import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load predefined keywords for roles
with open("data/roles_keywords.json", "r") as f:
    ROLES_KEYWORDS = json.load(f)

def score_resume(resume_text, job_description, role):
    keywords = ROLES_KEYWORDS.get(role.lower(), [])
    
    if job_description:
        # Compare with job description
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, job_description])
        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
        feedback = f"Similarity with job description: {similarity:.2%}"
        score = similarity * 10  # Normalize to a 0-10 scale for progress bar
    else:
        # Keyword-based scoring
        score = sum(1 for keyword in keywords if keyword in resume_text)
        feedback = f"Keyword match score: {score}/{len(keywords)}"
    
    return feedback, score

