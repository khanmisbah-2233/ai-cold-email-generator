import pandas as pd
from src.config import RAW_PORTFOLIO_PATH

REQUIRED_COLUMNS = ["project_name", "skills", "description", "link"]

def load_portfolio(path=RAW_PORTFOLIO_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in portfolio.csv: {missing}")

    return df.fillna("")