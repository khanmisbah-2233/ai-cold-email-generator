import streamlit as st
import pandas as pd
from src.config import RAW_PORTFOLIO_PATH
from src.services.portfolio_service import prepare_portfolio_vector_store

st.title("📁 Portfolio Manager")

st.write("Current portfolio data:")

try:
    df = pd.read_csv(RAW_PORTFOLIO_PATH)
    st.dataframe(df)

    if st.button("Refresh ChromaDB"):
        prepare_portfolio_vector_store()
        st.success("Portfolio vector database refreshed.")

except Exception as e:
    st.error(str(e))