#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
# ]
# ///
"""
Fetch a sample of the customer support ticket dataset and save it as CSV.

Usage:
    uv run fetch_tickets.py
"""

import json
import httpx
import pandas as pd

BASE_URL = "https://datasets-server.huggingface.co/rows"
DATASET = "Tobi-Bueck/customer-support-tickets"


def fetch_rows(offset: int = 0, length: int = 100) -> list[dict]:
    response = httpx.get(
        BASE_URL,
        params={
            "dataset": DATASET,
            "config": "default",
            "split": "train",
            "offset": offset,
            "length": length,
        },
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    # Each row is wrapped in {"row_idx": ..., "row": {...}, "truncated_cells": [...]}
    return [item["row"] for item in data["rows"]]


def main():
    print("Fetching 100 tickets...")
    rows = fetch_rows(offset=0, length=100)

    df = pd.DataFrame(rows)
    print(f"Fetched {len(df)} rows")
    print(f"Columns: {list(df.columns)}")
    print(f"\nPriority distribution:\n{df['priority'].value_counts()}")
    print(f"\nType distribution:\n{df['type'].value_counts()}")

    df.to_csv("sample_tickets.csv", index=False)
    print("\nSaved to sample_tickets.csv")


if __name__ == "__main__":
    main()