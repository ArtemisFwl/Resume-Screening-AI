"""
Resume Screening AI

Main entry point of the application.
This file orchestrates the complete resume screening pipeline.
"""

from src.resume_parser import extract_text_from_pdf
from src.text_cleaner import clean_text
from src.skill_extractor import extract_skills
from src.matcher import calculate_match_score

import os

RESUME_FOLDER = "data/resumes"
JOB_DESCRIPTION_PATH = "data/job_description/jd.pdf"

pdf_files = [
    os.path.join(RESUME_FOLDER, file)
    for file in os.listdir(RESUME_FOLDER)
    if file.endswith(".pdf")
]

job_description = extract_text_from_pdf(JOB_DESCRIPTION_PATH)
job_description = clean_text(job_description)

results = []
for pdf_file in pdf_files:
    raw_text = extract_text_from_pdf(pdf_file)
    cleaned_text = clean_text(raw_text)
    detected_skills = extract_skills(cleaned_text)
    match_score = calculate_match_score(cleaned_text, job_description)
    results.append((os.path.basename(pdf_file), match_score))

results.sort(key=lambda x: x[1], reverse=True)


print("\n" + "=" * 40)
print("CANDIDATE RANKING")
print("=" * 40)

for rank, (resume_name, score) in enumerate(results, start=1):
    print(f"{rank}. {resume_name} --> {score}%")


