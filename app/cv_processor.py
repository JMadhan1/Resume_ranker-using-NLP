import os
from PyPDF2 import PdfReader
import re

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''  # Ensure we handle cases where page text may be None
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ""

# Function to preprocess text (clean and normalize)
def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove excessive whitespaces
    text = text.strip()  # Strip leading and trailing whitespaces
    return text.lower()  # Normalize to lowercase for better matching

# Function to rank CVs (dummy scoring logic)
def rank_cvs(cv_text, job_description):
    cv_words = set(cv_text.split())  # Split CV text into words
    job_words = set(job_description.split())  # Split job description into words
    common_words = cv_words & job_words  # Intersection of words (common words)
    score = len(common_words)  # Use the count of common words as score
    return score

# Function to process all CVs and store their scores
def process_and_save_scores(upload_folder, job_description, output_file='cv_score.output'):
    scores = []
    
    # Loop through all PDF files in the upload folder
    for filename in os.listdir(upload_folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(upload_folder, filename)
            
            # Extract and process the text from each CV
            cv_text = extract_text_from_pdf(file_path)
            if cv_text:  # Only rank if text was extracted successfully
                cv_text = preprocess_text(cv_text)
                # Rank the CV against the job description
                score = rank_cvs(cv_text, preprocess_text(job_description))
                scores.append((filename, score))
    
    # Sort scores in descending order (highest score first)
    scores.sort(key=lambda x: x[1], reverse=True)
    
    # Save the scores to the output file
    try:
        with open(output_file, 'w') as f:
            for filename, score in scores:
                f.write(f'{filename}: {score}\n')
        print(f"Scores saved to {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")
    
    return scores  # Return scores for further use if needed
