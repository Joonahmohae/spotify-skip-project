"""
What goes here: 
- File paths (data/raw/...)
- List of Spotify JSON filenames
- Column names you want to keep
- Output filenames (like spotify_features.parquet)
- Project rules (like SESSION_GAP_MINUTES = 30)
"""

from pathlib import Path

DATA_DIR = Path("data/raw/Spotify_data")

AUDIO_FILES = [
    DATA_DIR / "Streaming_History_Audio_2019-2025_0.json",
    DATA_DIR / "Streaming_History_Audio_2025_1.json",
    DATA_DIR / "Streaming_History_Audio_2025-2026_2.json",
    ]

BASE_COLUMNS = [
    "ts",
    "ms_played",
    "conn_country",
    "master_metadata_album_artist_name",
    "reason_start",
    "reason_end",
    "shuffle",
    "skipped",
    "offline",
    ]
SESSION_GAP_MiNUTES = 30 
