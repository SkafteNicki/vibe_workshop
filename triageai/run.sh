#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$SCRIPT_DIR"

if [ -f "$SCRIPT_DIR/.env" ]; then
  set -a
  # Load local environment variables such as OPENROUTER_API_KEY.
  . "$SCRIPT_DIR/.env"
  set +a
fi

uv sync
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
