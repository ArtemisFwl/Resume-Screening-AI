import re
  
def clean_text(text):
    """
    Cleans raw resume text extracted from PDF.
    Removes unwanted PDF artifacts and prepares text for NLP.
    """
    # Remove PDF encoding artifacts like:
    # (cid:44476), (cid:44562), etc.
    text=re.sub(r'\(cid:\d+\)', ' ', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    # Convert text to lowercase for NLP processing
    text = text.lower()


    return text