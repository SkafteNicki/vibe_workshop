import json
import os
from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field


APP_DIR = Path(__file__).parent
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = os.getenv("OPENROUTER_MODEL", "anthropic/claude-sonnet-4.1")

TRIAGE_PROMPT = """
You are a support ticket triage assistant.

Read the customer ticket and return a JSON object with this exact shape:
{
  "priority": "Critical|High|Medium|Low",
  "category": "Billing|Bug|Feature Request|Account|Other",
  "sentiment": "Frustrated|Neutral|Positive",
  "summary": "1-2 sentence plain-English summary",
  "draft_reply": "Professional, empathetic first response in 2-4 short paragraphs",
  "escalate": true,
  "escalate_reason": "One-sentence justification"
}

Rules:
- Return valid JSON only.
- Do not wrap the JSON in markdown fences.
- Choose the closest category from the allowed list.
- Use Critical only for severe urgency, threats of chargebacks, legal risk, outages, or account lockout emergencies.
- Use escalate=true when the ticket likely needs urgent human review, refund handling, specialist attention, or leadership visibility.
- Keep the summary concise and plain English.
- Keep the draft reply professional, calm, and empathetic.
""".strip()


class TriageRequest(BaseModel):
    text: str = Field(min_length=1)
    api_key: str | None = None


class TriageResult(BaseModel):
    priority: str
    category: str
    sentiment: str
    summary: str
    draft_reply: str
    escalate: bool
    escalate_reason: str


app = FastAPI(title="TriageAI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=APP_DIR), name="static")


def extract_json_block(text: str) -> dict:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("Model response did not contain JSON")
    return json.loads(text[start : end + 1])


async def call_openrouter(ticket_text: str, api_key: str) -> TriageResult:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/codespaces",
        "X-Title": "TriageAI Workshop Prototype",
    }
    payload = {
        "model": DEFAULT_MODEL,
        "messages": [
            {"role": "system", "content": TRIAGE_PROMPT},
            {"role": "user", "content": ticket_text},
        ],
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
    }

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(OPENROUTER_URL, headers=headers, json=payload)

    if response.status_code >= 400:
        detail = response.text
        raise HTTPException(status_code=502, detail=f"OpenRouter request failed: {detail}")

    data = response.json()
    try:
        message = data["choices"][0]["message"]["content"]
        parsed = extract_json_block(message)
        return TriageResult.model_validate(parsed)
    except (KeyError, IndexError, ValueError, json.JSONDecodeError) as exc:
        raise HTTPException(status_code=502, detail=f"Could not parse model response: {exc}") from exc


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(APP_DIR / "index.html")


@app.get("/health")
async def health() -> dict:
    return {"ok": True, "model": DEFAULT_MODEL}


@app.post("/triage", response_model=TriageResult)
async def triage(request: TriageRequest) -> TriageResult:
    api_key = request.api_key or os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=400,
            detail="Missing OpenRouter API key. Set OPENROUTER_API_KEY or paste a key into the page.",
        )

    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Ticket text cannot be empty.")

    return await call_openrouter(text, api_key)
