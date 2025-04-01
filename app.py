import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Check digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    
    # Check special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Blacklist common passwords
    common_passwords = {"password123", "12345678", "qwerty", "letmein", "welcome"}
    if password.lower() in common_passwords:
        return "Weak", "Your password is too common. Choose a more unique one."
    
    # Determine strength level
    if score <= 2:
        return "Weak", feedback
    elif score <= 4:
        return "Moderate", feedback
    else:
        return "Strong", "Your password is strong!"

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        strength, feedback = check_password_strength(password)
        st.subheader(f"Password Strength: {strength}")
        
        if isinstance(feedback, list):
            st.write("### Suggestions to improve your password:")
            for tip in feedback:
                st.write(f"- {tip}")
            st.write(f"Suggested strong password: `{generate_strong_password()}`")
        else:
            st.success(feedback)
    else:
        st.error("Please enter a password.")
