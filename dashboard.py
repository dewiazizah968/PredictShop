import streamlit as st
import base64
import time

def dashboard_page():
    with open("assets/logo.png", "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    # WARNING 3 detik
    warning_container = st.empty()
    with warning_container:
        st.warning("For best experience, please switch to light mode!", icon="⚠️")
    time.sleep(3)
    warning_container.empty()

    # CSS Styling
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: #FFF1E0;
            }}
            .header-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 70px;
                margin-bottom: 50px;
                gap: 20px;
            }}
            .logo {{
                width: 100px;
                height: auto;
            }}
            .title {{
                font-size: 90px;
                font-weight: bold;
                color: #000000;
                margin: 0;
            }}
            .stButton>button {{
                background-color: #FFA500;
                color: black;
                font-weight: bold;
                padding: 18px 40px;
                border-radius: 10px;
                border: none;
                font-size: 30px !important;
                min-width: 180px;
                margin: 10px;
                text-align: center;
                cursor: pointer;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="header-container">
            <img src="data:image/png;base64,{encoded_logo}" class="logo">
            <div class="title">Predict Shop</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5 = st.columns([3, 2.5, 0.3, 2, 2])
    with col2:
        if st.button("🔐 Log in"):
            st.session_state["logged_in"] = False
            st.session_state["start"] = True
            st.session_state["signup"] = False
            st.rerun()
    with col4:
        if st.button("🧾 Sign Up"):
            st.session_state["logged_in"] = False
            st.session_state["start"] = True
            st.session_state["signup"] = True
            st.rerun()
