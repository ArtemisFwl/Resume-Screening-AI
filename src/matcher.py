def calculate_match_score(resume_text, job_description):
    """
    Calculates the similarity score between a resume and a job description.
    """
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    common_words = 0
    for word in job_description.split():
     if word in resume_text:
        common_words += 1

    total_words = len(job_description.split())
    score = (common_words / total_words) * 100

    return round(score, 2)