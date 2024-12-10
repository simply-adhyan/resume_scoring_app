import PyPDF2
import docx

def parse_resume(file):
    text = ""
    if file.name.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
    return text.lower()

def parse_job_description(text):
    # Clean and normalize job description text
    return text.lower().strip()
