"""
Resume Screening AI

Main entry point of the application.
This file orchestrates the complete resume screening pipeline.
"""

from src.resume_parser import extract_text_from_pdf
from src.text_cleaner import clean_text
from src.skill_extractor import extract_skills
from src.matcher import calculate_match_score

pdf_file = "data/sample_resume.pdf"

raw_text = extract_text_from_pdf(pdf_file)
cleaned_text = clean_text(raw_text)
detected_skills = extract_skills(cleaned_text)

print("Cleaned Text")
print(cleaned_text[:500])

job_description = """
Looking for a Data Scientist with experience in Python, Machine Learning,
TensorFlow, Pandas, NumPy, SQL, Git, and data analysis.
"""
match_score = calculate_match_score(cleaned_text, job_description)
print(f"\nMatch Score: {match_score}%")

print("\nDetected Skills:")
for skill in detected_skills:
    print(f"- {skill}")