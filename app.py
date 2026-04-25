import streamlit as st

from src.services.portfolio_service import prepare_portfolio_vector_store
from src.services.email_service import generate_cold_email

st.set_page_config(
    page_title="AI Cold Email Generator",
    page_icon="📧",
    layout="wide"
)

st.title("📧 AI-Powered Cold Email Generator")
st.write("Paste a job description and generate a personalized cold email using your portfolio.")

with st.sidebar:
    st.header("Portfolio Setup")

    if st.button("Build / Refresh Portfolio Database"):
        try:
            df = prepare_portfolio_vector_store()
            st.success(f"Portfolio database created with {len(df)} projects.")
        except Exception as e:
            st.error(str(e))

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste job description here..."
)

if st.button("Generate Cold Email"):
    try:
        with st.spinner("Searching portfolio and generating email..."):
            email, relevant_docs = generate_cold_email(job_description)

        st.subheader("Generated Cold Email")
        st.text_area("Email Output", value=email, height=300)

        st.subheader("Matched Portfolio Projects")
        for doc in relevant_docs:
            st.info(doc.page_content)

    except Exception as e:
        st.error(str(e))