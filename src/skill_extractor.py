 # List of skills that our system can identify
SKILLS = [
    "python",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "keras",
    "machine learning",
    "deep learning",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "matplotlib",
    "opencv",
    "streamlit",
    "git",
    "github",
    "sap"
    ]


def extract_skills(text):
    
    detected_skills = []

    for skill in SKILLS:
        if skill in text:
            detected_skills.append(skill)
    
    return detected_skills

    