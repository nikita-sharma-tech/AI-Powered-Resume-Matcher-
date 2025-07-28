# resume_match_backend.py

import re, codecs, string
from PyPDF2 import PdfReader
import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

nltk.download('punkt')
nltk.download('wordnet')

# Load Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Optional fallback keywords list for visible feedback
important_keywords = [
    'python', 'machine learning', 'nlp', 'sql', 'data analysis', 'deep learning',
    'pandas', 'excel', 'communication', 'teamwork', 'problem solving',
    'tensorflow', 'keras', 'sklearn', 'visualization', 'power bi', 'leadership'
]


def read_resume(pdf_file, isJDFile):
    pdf_reader = PdfReader(pdf_file)
    content = "\n".join(page.extract_text().strip() for page in pdf_reader.pages if page.extract_text())
    content = ' '.join(content.split())
    content = content.encode('ascii', 'ignore')
    if isinstance(content, bytes):
        content = content.decode('utf-8')
    return clean_text(content, isJDFile)


def read_job_description(txt_file, isJDFile):
    if isinstance(txt_file, str):
        with open(txt_file, 'r', encoding='utf-8') as f:
            jobDescription = f.read()
    else:
        jobDescription = txt_file.read()

    jobDescription = jobDescription.replace(codecs.BOM_UTF8.decode(), '') if jobDescription.startswith(codecs.BOM_UTF8.decode()) else jobDescription
    jobDescription = jobDescription.encode('ascii', 'ignore').decode()
    return clean_text(jobDescription, isJDFile)


def clean_text(text, isJDFile):
    text = text.lower()
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '', text)
    text = re.sub(r'[\/;:.,\-]', ' ', text)
    text = ''.join(ch for ch in text if ch not in set(string.punctuation))
    text = re.sub(r'\d', '', text)
    return stem_and_remove_stopwords(text, isJDFile)


def stem_and_remove_stopwords(text, isJDFile):
    tokens = text.split()
    stop_words = set(ENGLISH_STOP_WORDS)
    tokens = [word for word in tokens if word not in stop_words and len(word) > 1]

    lemmatizer = WordNetLemmatizer()
    stemmed_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    stemmed_tokens = [LancasterStemmer().stem(word) for word in stemmed_tokens]

    final_text = " ".join(stemmed_tokens)

    if isJDFile == 'Y':
        stemmedWordsDict = {PorterStemmer().stem(word): word for word in stemmed_tokens}
        return final_text, stemmedWordsDict
    else:
        return final_text


def calculate_percent_match(resume_text, jd_text, stemmed_dict=None):
    # Use sentence transformer embeddings
    resume_embed = model.encode(resume_text, convert_to_tensor=True)
    jd_embed = model.encode(jd_text, convert_to_tensor=True)

    # Calculate cosine similarity
    similarity = util.pytorch_cos_sim(resume_embed, jd_embed).item()
    score = round(similarity * 100, 2)

    # Keyword match (optional for visual feedback only)
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())
    matched_terms = [kw for kw in important_keywords if any(kw in word for word in resume_words)]
    unmatched_terms = [kw for kw in important_keywords if kw not in matched_terms]

    return score, matched_terms, unmatched_terms
