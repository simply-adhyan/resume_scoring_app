import streamlit as st
from dotenv import load_dotenv
import os
import smtplib
from random import randint

# Load environment variables from .env file
load_dotenv()

# Function to send OTP
def send_otp(email):
    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")
    otp = randint(100000, 999999)
    st.session_state["otp"] = str(otp)  # Store OTP as a string for comparison

    subject = "OTP for Logging In"
    body = f"Your OTP for logging in is {otp}."

    message = f"Subject: {subject}\n\n{body}"

    try:
        # Connect to SMTP server
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(sender_email, app_password)
        
        # Send the email
        connection.sendmail(from_addr=sender_email, to_addrs=email, msg=message)
        connection.close()
        st.success(f"OTP sent to {email}!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# Function to authenticate user
def authenticate_user():
    # Input for email
    email = st.text_input("Enter your email:")

    # Button to send OTP
    if st.button("Send OTP"):
        if email:
            send_otp(email)
        else:
            st.error("Please enter an email address.")

    # Input for OTP
    otp_input = st.text_input("Enter OTP:")

    # Button to verify OTP
    if st.button("Verify OTP"):
        if otp_input == st.session_state.get("otp", ""):
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid OTP. Please try again.")
            return False

    return False
