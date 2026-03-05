import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

def load_data():
    # Change filename if yours is different
    file = RAW_PATH / "superstore.csv"
    df = pd.read_csv(file, encoding="latin-1")  # superstore sometimes needs latin-1
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_").replace("-", "_") for c in df.columns]

    # Convert date columns if present
    for col in ["order_date", "ship_date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values (basic)
    df = df.dropna(subset=[c for c in ["sales", "profit"] if c in df.columns])

    return df

def save_clean_data(df: pd.DataFrame):
    out_file = PROCESSED_PATH / "superstore_clean.csv"
    df.to_csv(out_file, index=False)
    print(f"✅ Cleaned data saved to: {out_file}")

if __name__ == "__main__":
    df_raw = load_data()
    df_clean = clean_data(df_raw)
    save_clean_data(df_clean)
    print("Rows raw:", len(df_raw))
    print("Rows clean:", len(df_clean))