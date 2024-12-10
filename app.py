import streamlit as st
from utils.auth import authenticate_user
from utils.file_processing import parse_resume, parse_job_description
from utils.scoring import score_resume
from utils.visualization import display_results

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Login page
if not st.session_state["logged_in"]:
    st.title("Login")
    if authenticate_user():
        st.session_state["logged_in"] = True
else:
    # Main app
    st.title("Resume Scoring Application")
    
    # Step 1: Upload Resume
    st.header("Step 1: Upload Resume")
    resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    if resume_file:
        resume_text = parse_resume(resume_file)
        st.success("Resume uploaded successfully!")

        # Step 2: Job Description (Optional)
        st.header("Step 2: Job Description (Optional)")
        job_description = st.text_area("Paste the job description here:")
        
        # Step 3: Select Role
        st.header("Step 3: Select Role")
        role = st.selectbox("Select a role", ["Software Engineer", "Data Scientist", "Custom"])
        if role == "Custom":
            role = st.text_input("Enter your custom role:")
        
        if st.button("Analyze"):
            # Scoring
            feedback, score = score_resume(resume_text, job_description, role)
            display_results(feedback, score)
