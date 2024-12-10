import streamlit as st

def display_results(feedback, score):
    st.subheader("Results")
    st.write(feedback)
    st.progress(score / 10)  # Assuming a score out of 10
