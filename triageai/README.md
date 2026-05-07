# TriageAI Solution

This is a small reference implementation for the workshop case.

## What It Includes

- `main.py`: FastAPI backend and OpenRouter integration
- `index.html`: single-page frontend
- `pyproject.toml`: Python dependencies managed by `uv`

## Run It In Codespaces

From the `triageai/` folder, run:

```bash
./run.sh
```

Then open the forwarded port for `8000` in Codespaces.

If you place a `.env` file in `triageai/`, `./run.sh` will load it automatically before starting the app.

If you prefer to run the steps manually:

```bash
uv sync
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

If your Codespace was created before the latest devcontainer changes, rebuild it first so `uv` is available in the terminal.

## OpenRouter Key

The app supports two ways to provide the key:

1. Set `OPENROUTER_API_KEY` in the environment before starting the server
2. Paste the key into the page before clicking `Triage Ticket`

The second option is useful for workshop demos because it works even if the backend environment is not pre-configured.
