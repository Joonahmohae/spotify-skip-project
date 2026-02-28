from src.config import AUDIO_FILES, BASE_COLUMNS
from src.io import load_many_json
from src.io import to_parquet
from src.clean import build_base_table


def main() -> None:
    raw_df = load_many_json(AUDIO_FILES)
    filtered_df = build_base_table(raw_df, BASE_COLUMNS)

    # cleaned_events_df (parquet) = df with ts reflecting timezone, ms converted to seconds or minutes to align with the sessioning (Seconds or minutes), 
    # features_table_df (parquet) = also confused

    #to_parquet(cleaned_events_df, path)
    #to_parquest(features_table_df, path)

    print(filtered_df.head(10))
    print(filtered_df.shape)


if __name__ == "__main__":
    main()








