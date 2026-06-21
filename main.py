"""
Resume Screening AI

Main entry point of the application.
This file orchestrates the complete resume screening pipeline.
"""

from src.resume_parser import extract_text_from_pdf
from src.text_cleaner import clean_text

pdf_file = "data/sample_resume.pdf"

raw_text = extract_text_from_pdf(pdf_file)
cleaned_text = clean_text(raw_text)

print(cleaned_text[:500])