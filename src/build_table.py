import json
from pathlib import Path
import pandas as pd

DATA_DIR = Path("Spotify_data")

AUDIO_FILES = [DATA_DIR/ "Streaming_History_Audio_2019-2025_0.json", 
               DATA_DIR/ "Streaming_History_Audio_2025_1.json", 
               DATA_DIR/ "Streaming_History_Audio_2025-2026_2.json"]

def load_one_json(path: Path) -> pd.DataFrame:
    with open(path, "r", encoding = "utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    return df

dfs = []

for i in range(len(AUDIO_FILES)):
    df = load_one_json(AUDIO_FILES[i])
    dfs.append(df)

concat_df = pd.concat(dfs)

# columns we need: ts, ms_played, conn_country, master_metadata_album_artist_name, reason_start, reason_end, shuffle, skipped, offline
filtered_df = concat_df[["ts", "ms_played", "conn_country", "master_metadata_album_artist_name", "reason_start", "reason_end", "shuffle", "skipped", "offline"]].copy()
filtered_df["ts"] = pd.to_datetime(filtered_df["ts"], utc=True)
filtered_df = filtered_df.sort_values("ts")

print(filtered_df.head(10))








