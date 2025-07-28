# AI-Powered Resume Matcher

## Overview
- This project is an AI-powered desktop application designed to evaluate how well a candidate’s resume matches a given job description.  
- Using Natural Language Processing (NLP) and keyword-based text analytics, it calculates a match score and highlights matched and unmatched terms.  
- The application features a clean and user-friendly GUI built using **Tkinter** with **ttkbootstrap** for modern styling.

---

## Key Features
- Upload resume (PDF) and job description (TXT) files easily.
- NLP-based keyword extraction and preprocessing (tokenization, stemming, stopword removal).
- Generates a **Match Score (%)** indicating resume-job relevance.
- Displays matched and unmatched terms in scrollable, color-coded panels.
- Offline functionality after initial setup.

---

## Tech Stack
- **Programming Language:** Python 3.10+
- **GUI Framework:** Tkinter with ttkbootstrap theme
- **NLP Libraries:** NLTK, Regex
- **PDF Handling:** PyPDF2 or pdfminer.six

---

## Installation

1. **Clone repository**: <br>
git clone <your-repo-link>

2. **Navigate to project folder**: <br>
cd resume-matcher

3. **Create virtual environment**:<br>
python -m venv env <br>
env\Scripts\activate  # Windows <br>

4. **Install dependencies**: <br>
pip install -r requirements.txt

---

## Usage
python app.py

- Upload resume in PDF format.

- Upload job description in TXT format.

- Click Check Match to view score and keyword breakdown.

---

## Project Structure <br>
├── app.py                          # Main application file <br>
├── resume_match_backend            # Matching and NLP logic <br>
├──JobDescription.txt               # Sample job description  <br>
├── requirements.txt                # Python dependencies     <br>
├──Sample_Resume.pdf                # This is sample resume <br>
└── README.md                       # Project documentation    <br>

---

## Sample Output

![Sample Output](https://github.com/user-attachments/assets/ac3f9417-51b8-4460-ac61-ec52e72e4e72)



## Future Scope
- Semantic matching using AI models (e.g., BERT).

- Batch resume processing and ranking.

- Cloud/web-based deployment and ATS integration.

## About Me
Hi, I’m **Nikita Sharma**, a CSE student passionate about AI and building smart solutions.  

## Contributing
Contributions are welcome!  
- Fork the repo  
- Make changes  
- Open a pull request  

If you like this project, **give it a ⭐ and share your feedback!**
