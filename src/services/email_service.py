from src.services.job_service import validate_job_description
from src.vector_db.chroma_manager import search_relevant_projects
from src.chains.email_chain import generate_email_with_llm

def format_portfolio_context(documents):
    if not documents:
        return "No relevant portfolio project found."

    return "\n\n".join([doc.page_content for doc in documents])

def generate_cold_email(job_description: str):
    job_description = validate_job_description(job_description)

    relevant_docs = search_relevant_projects(job_description)
    portfolio_context = format_portfolio_context(relevant_docs)

    email = generate_email_with_llm(
        job_description=job_description,
        portfolio_context=portfolio_context
    )

    return email, relevant_docs