# Resume Screening AI

An AI-powered Applicant Tracking System (ATS) that automatically analyzes resumes against a job description, extracts relevant skills, calculates an ATS match score using TF-IDF and Cosine Similarity, and ranks candidates based on their suitability for the role.

## Features

- Parse resumes from PDF files
- Parse Job Description (JD) from PDF
- Clean and preprocess text
- Extract technical skills
- Calculate ATS Match Score using TF-IDF and Cosine Similarity
- Identify matched and missing skills
- Process multiple resumes in a single run
- Rank candidates based on ATS score

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF, Cosine Similarity |
| PDF Processing | pdfplumber |
| Version Control | Git, GitHub |
| IDE | Visual Studio Code |

## Project Architecture

```text
                  +----------------------+
                  | Job Description PDF  |
                  +----------+-----------+
                             |
                             v
                    PDF Text Extraction
                             |
                             v
                      Text Cleaning
                             |
                             |
+----------------------+     |
|    Resume PDF(s)     |-----+
+----------+-----------+
           |
           v
    PDF Text Extraction
           |
           v
      Text Cleaning
           |
           v
     Skill Extraction
           |
           v
TF-IDF Vectorization + Cosine Similarity
           |
           v
      ATS Match Score
           |
           v
 Candidate Ranking & Results
```

## Folder Structure

```text
Resume-Screening-AI/
│
├── app/
├── data/
│   ├── job_description/
│   │   └── jd.pdf
│   └── resumes/
│       ├── resume1.pdf
│       ├── resume2.pdf
│       └── resume3.pdf
│
├── models/
├── notebooks/
│
├── src/
│   ├── resume_parser.py
│   ├── text_cleaner.py
│   ├── skill_extractor.py
│   └── matcher.py
│
├── main.py
├── requirements.txt
└── README.md
```


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/artemisfwl/Resume-Screening-AI.git
```

### 2. Navigate to the project folder

```bash
cd Resume-Screening-AI
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

## Future Improvements

- Build a Streamlit web application
- Support DOCX resume parsing
- Use Sentence Transformers for semantic matching
- Extract experience and education automatically
- Export results to CSV/Excel
- Add LLM-powered resume feedback
- Deploy the application on Streamlit Cloud

## Author

**Aman Deep**

- GitHub: https://github.com/artemisfwl
- LinkedIn: https://www.linkedin.com/in/aman-deep-artemisfowl/