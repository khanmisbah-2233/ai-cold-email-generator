from langchain_core.prompts import ChatPromptTemplate

EMAIL_PROMPT = ChatPromptTemplate.from_template("""
You are a professional cold email writer.

Write a short, natural, and personalized cold email for a job application.

Job Description:
{job_description}

Relevant Portfolio Projects:
{portfolio_context}

Rules:
- Keep it professional.
- Do not exaggerate.
- Mention only relevant experience.
- Keep it under 180 words.
- Add a clear call to action.
- Do not use fake claims.

Generate the final cold email:
""")