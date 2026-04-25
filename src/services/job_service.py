def validate_job_description(job_description: str):
    if not job_description or not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    if len(job_description.strip()) < 30:
        raise ValueError("Job description is too short. Paste a proper job description.")

    return job_description.strip()