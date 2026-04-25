from src.data.portfolio_loader import load_portfolio
from src.data.data_cleaner import clean_portfolio
from src.vector_db.chroma_manager import build_vector_store

def prepare_portfolio_vector_store():
    df = load_portfolio()
    clean_df = clean_portfolio(df)
    build_vector_store(clean_df)
    return clean_df