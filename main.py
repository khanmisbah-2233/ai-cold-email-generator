"""
Main CLI entry point for AI Cold Email Generator.

This file is used to test the backend workflow without running Streamlit.
For the web app, run: streamlit run app.py
"""

from src.logger import logger
from src.services.portfolio_service import prepare_portfolio_vector_store
from src.services.email_service import generate_cold_email


def print_separator(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def get_job_description_from_user() -> str:
    print_separator("Paste Job Description")
    print("Paste the full job description below.")
    print("When finished, press ENTER twice:\n")

    lines = []

    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    return "\n".join(lines).strip()


def show_matched_projects(relevant_docs) -> None:
    print_separator("Matched Portfolio Projects")

    if not relevant_docs:
        print("No relevant portfolio projects found.")
        return

    for index, doc in enumerate(relevant_docs, start=1):
        print(f"\nProject Match #{index}")
        print("-" * 50)
        print(doc.page_content)


def show_generated_email(email: str) -> None:
    print_separator("Generated Cold Email")
    print(email)


def main() -> None:
    try:
        print_separator("AI Cold Email Generator - CLI Mode")

        logger.info("Preparing portfolio vector database...")
        print("Preparing portfolio database...")

        portfolio_df = prepare_portfolio_vector_store()

        print(f"Portfolio database ready. Total projects loaded: {len(portfolio_df)}")
        logger.info("Portfolio vector database prepared successfully.")

        job_description = get_job_description_from_user()

        if not job_description:
            print("Job description is empty. Please run again and paste a valid job description.")
            return

        print("\nSearching portfolio and generating cold email...")
        logger.info("Generating cold email from job description.")

        email, relevant_docs = generate_cold_email(job_description)

        show_matched_projects(relevant_docs)
        show_generated_email(email)

        logger.info("Cold email generated successfully.")

    except KeyboardInterrupt:
        print("\nProcess stopped by user.")
        logger.warning("CLI process interrupted by user.")

    except Exception as error:
        print("\nSomething went wrong:")
        print(error)
        logger.exception("Error occurred in main CLI workflow.")


if __name__ == "__main__":
    main()