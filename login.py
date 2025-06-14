import streamlit as st
import pandas as pd
import os

def login_page():
    # CSS styling
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #FFF1E0;
            }
            .stButton>button {
                background-color: #FFA500;
                color: black;
                font-weight: bold;
                padding: 18px 40px;
                border-radius: 10px;
                border: none;
                font-size: 35px !important;
                min-width: 180px;
                margin-top: 20px;
                text-align: center;
                cursor: pointer;
            }
            .title {
                font-size: 80px;
                font-weight: bold;
                color: black;
                text-align: center;
                margin-bottom: 30px;
            }
            /* Gaya untuk input text dan password */
            input[type="text"], input[type="password"] {
                background-color: white !important;
                color: black !important;
                border: 1px solid #ccc !important;
                border-radius: 8px !important;
                padding: 10px !important;
                font-size: 18px !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='title'>Login</div>", unsafe_allow_html=True)

    # Input Form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("🔐 Login"):
        if os.path.exists("users.csv"):
            df_users = pd.read_csv("users.csv", dtype=str)

            df_users["Username"] = df_users["Username"].str.strip().str.lower()
            df_users["Password"] = df_users["Password"].str.strip()

            username_input = username.strip().lower()
            password_input = password.strip()

            match = df_users[
                (df_users["Username"] == username_input) &
                (df_users["Password"] == password_input)
            ]

            if not match.empty:
                st.success("Login successful!")
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Invalid username or password.")
        else:
            st.warning("No users found. Please sign up first.")