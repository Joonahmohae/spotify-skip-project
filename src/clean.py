"""
what goes here:
- select only the columns you care about
- convert ts to datetime
- sort rows by time
- clean boolean columns (shuffle, skipped, offline)
- handle missing values
- remove obviously invalid rows (if needed)
"""

import pandas as pd

def build_base_table(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df[columns].copy()
    out["ts"] = pd.to_datetime(out["ts"], utc=True)
    out = out.sort_values("ts").reset_index(drop=True)
    return out

def convert_ts(df: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Will implement later")


def convert_ms(df: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError("Will implement later")

def sort_rows(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    raise NotImplementedError("Will implement later")

def convert_boolean(df: pd.DataFrame, columns: list[str]):
    raise NotImplementedError("Will implement later")