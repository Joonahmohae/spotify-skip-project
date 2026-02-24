---
output:
  pdf_document: default
  html_document: default
---
# Spotify Skip Prediction (Data Pipeline + Feature Engineering)

Built an end-to-end data pipeline that transforms raw Spotify streaming JSON logs into a cleaned, time-ordered dataset and engineers session-level + sequential features for skip prediction.

## Project Goals
- Parse and normalize raw Spotify streaming history (JSON file)
- Clean + standardize timestamps, track identifiers, and playback fields
- Build sessionized listening sequences
- Engineer features (track order, skips, listening duration, context)
- Export feature-ready tables for modeling + EDA

## Repository Structure
- `data/raw/` — raw Spotify JSON (ignored by git)
- `data/processed/` — cleaned outputs (csv/parquet)
- `src/` — reusable pipeline code
- `notebooks/` — analysis notebooks (01 → 04)
- `reports/` — EDA summaries and figures

## Quickstart
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt