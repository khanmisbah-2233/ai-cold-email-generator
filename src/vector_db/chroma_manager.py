from langchain_chroma import Chroma
from langchain_core.documents import Document

from src.config import CHROMA_DIR, COLLECTION_NAME
from src.embeddings.embedding_model import get_embedding_model

def create_documents(portfolio_df):
    documents = []

    for _, row in portfolio_df.iterrows():
        documents.append(
            Document(
                page_content=row["combined_text"],
                metadata={
                    "project_name": row["project_name"],
                    "skills": row["skills"],
                    "link": row["link"]
                }
            )
        )

    return documents

def build_vector_store(portfolio_df):
    embedding_model = get_embedding_model()
    documents = create_documents(portfolio_df)

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=str(CHROMA_DIR),
        collection_name=COLLECTION_NAME
    )

    return vector_store

def load_vector_store():
    embedding_model = get_embedding_model()

    return Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME
    )

def search_relevant_projects(job_description: str, top_k: int = 3):
    vector_store = load_vector_store()
    results = vector_store.similarity_search(job_description, k=top_k)
    return results