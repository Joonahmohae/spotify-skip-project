"""
what goes here:
- opens json file
- turns them into dataframe
- combine multiple files into one table
- saving cleaned results to parquet
"""

import json
from pathlib import Path
import pandas as pd

def load_one_json(path: Path) -> pd.DataFrame:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def load_many_json(paths: list[Path]) -> pd.DataFrame:
    dfs = []
    for path in paths:
        df = load_one_json(path)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

#example path: ("data/processed/spotify_events_clean.parquet")
def to_parquet(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents = True, exist_ok = True)
    df.to_parquet(path, index = False)