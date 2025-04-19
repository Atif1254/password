import streamlit as st
import re

st.title("🔐 Password Strength Meter")

# Password Input
password = st.text_input("Enter your password", type="password")

# Function to check password strength
def check_strength(pw):
    strength = 0
    remarks = ""

    # Conditions
    if len(pw) >= 8:
        strength += 1
    if re.search(r"[A-Z]", pw):
        strength += 1
    if re.search(r"[a-z]", pw):
        strength += 1
    if re.search(r"[0-9]", pw):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        strength += 1

    # Remarks based on score
    if strength <= 2:
        remarks = "Weak 😟"
        color = "red"
    elif strength == 3 or strength == 4:
        remarks = "Moderate 😐"
        color = "orange"
    else:
        remarks = "Strong 💪"
        color = "green"

    return strength, remarks, color

if password:
    strength, remarks, color = check_strength(password)
    st.markdown(f"**Strength Score:** {strength}/5")
    st.markdown(f"<h3 style='color:{color};'>{remarks}</h3>", unsafe_allow_html=True)