import streamlit as st
import pandas as pd
import random
import string
import os
import time
import re  

def generate_username(name, role):
    rand_num = ''.join(random.choices(string.digits, k=2))
    uname = f"{name[:3]}{role[:2]}{rand_num}".lower()
    return uname

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def is_valid_email(email):
    allowed_domains = ["@gmail.com", "@example.co.id", "@domain.org"]
    return any(email.endswith(domain) for domain in allowed_domains)

def signup_page():
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
                font-size: 30px !important;
                min-width: 180px;
                margin-top: 20px;
                text-align: center;
                cursor: pointer;
            }
            input[type="text"], input[type="email"] {
                background-color: white !important;
                color: black !important;
                border: 1px solid #ccc !important;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px !important;
            }
            .stSelectbox div[data-baseweb="select"] {
                background-color: white !important;
                color: black !important;
                border-radius: 8px;
                padding: 6px;
                font-size: 16px;
                border: 1px solid #ccc;
            }
            .title {
                font-size: 80px;
                font-weight: bold;
                color: black;
                text-align: center;
                margin-bottom: 30px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='title'>Sign Up</div>", unsafe_allow_html=True)

    # Form input
    name = st.text_input("Name")
    role = st.selectbox("Position", ["Admin", "Developer"])
    email = st.text_input("Email")

    if st.button("🧾 Create Account"):
        if name and email:
            if not is_valid_email(email):
                st.error("Invalid email domain. Use @gmail.com, @example.co.id, or @domain.org only.")
                return

            username = generate_username(name, role)
            password = generate_password()

            user_data = {
                "Name": name,
                "Role": role,
                "Email": email,
                "Username": username,
                "Password": password
            }

            df_new = pd.DataFrame([user_data])

            if os.path.exists("users.csv"):
                df_existing = pd.read_csv("users.csv", dtype=str)
                df_all = pd.concat([df_existing, df_new], ignore_index=True)
            else:
                df_all = df_new

            df_all.to_csv("users.csv", index=False)

            st.success(f"✅ Account created!\n\nYour username is `{username}` and password is `{password}`")
            st.session_state["logged_in"] = True
            time.sleep(5)
            st.rerun()
        else:
            st.warning("Please fill in all the fields.")