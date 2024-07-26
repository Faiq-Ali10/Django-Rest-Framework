from PyPDF2 import PdfReader
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        raise ValueError(f"Error reading PDF: {str(e)}")
    return text

def extract_nouns_verbs(text):
    # Basic example of extracting nouns and verbs
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # This is a basic example; in a real application, consider using a POS tagger
    nouns = [word for word in filtered_words if word.isalpha()]  # Placeholder for nouns extraction
    verbs = []  # Placeholder for verbs extraction
    
    return nouns, verbs

