from langchain_groq import ChatGroq
from src.config import GROQ_API_KEY, GROQ_MODEL
from src.chains.prompt_templates import EMAIL_PROMPT

def get_llm():
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing. Add it in .env file.")

    return ChatGroq(
        model=GROQ_MODEL,
        temperature=0.4,
        api_key=GROQ_API_KEY
    )

def generate_email_with_llm(job_description: str, portfolio_context: str) -> str:
    llm = get_llm()
    chain = EMAIL_PROMPT | llm
    response = chain.invoke({
        "job_description": job_description,
        "portfolio_context": portfolio_context
    })

    return response.content