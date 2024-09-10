import streamlit as st
import requests

# Backend API URL (Flask)
API_URL = "http://127.0.0.1:5000"

# Streamlit App
st.title("Streamlit Registration & Login")

# Registration
st.header("Register")
register_username = st.text_input("Enter username", key="register_username")
register_password = st.text_input("Enter password", type="password", key="register_password")
register_confirm_password = st.text_input("Confirm password", type="password", key="register_confirm_password")

if st.button("Register"):
    if register_password == register_confirm_password:
        # Send POST request to Flask API for registration
        register_data = {
            "username": register_username,
            "password": register_password,
            "confirm_password": register_confirm_password,
        }
        response = requests.post(f"{API_URL}/register", data=register_data)
        if response.status_code == 200:
            st.success("Registration successful! You can log in now.")
        else:
            st.error("Registration failed. Try a different username.")
    else:
        st.error("Passwords do not match!")

# Login
st.header("Login")
login_username = st.text_input("Enter username", key="login_username")
login_password = st.text_input("Enter password", type="password", key="login_password")

if st.button("Login"):
    # Send POST request to Flask API for login
    login_data = {
        "username": login_username,
        "password": login_password,
    }
    response = requests.post(f"{API_URL}/login", data=login_data)

    if response.status_code == 200:
        st.success(f"Logged in as {login_username}")
        st.session_state['logged_in'] = True
        st.session_state['username'] = login_username
    else:
        st.error("Login failed. Please check your credentials.")

# Logout
if 'logged_in' in st.session_state and st.session_state['logged_in']:
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.success("Logged out successfully!")
