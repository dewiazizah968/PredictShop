import streamlit as st
from dashboard import dashboard_page
from signup import signup_page
from login import login_page
from input import input_page
from history import history_page
from info import info_page

st.set_page_config(page_title="Predict Shop", layout="wide")

if "start" not in st.session_state:
    st.session_state["start"] = False

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def main():
    if not st.session_state["start"]:
        hide_sidebar = """
        <style>
            [data-testid="stSidebar"] {display: none;}
            [data-testid="stHeader"] {display: none;}
        </style>
        """
        st.markdown(hide_sidebar, unsafe_allow_html=True)
        dashboard_page()

    elif st.session_state["start"] and not st.session_state["logged_in"]:
        hide_sidebar = """
        <style>
            [data-testid="stSidebar"] {display: none;}
            [data-testid="stHeader"] {display: none;}
        </style>
        """
        st.markdown(hide_sidebar, unsafe_allow_html=True)

        if "signup" in st.session_state and st.session_state["signup"]:
            signup_page()
        else:
            login_page()

    else:
        # Styling halaman utama
        st.markdown(
            """
            <style>
            body {
                background-color: #FFF1E0 !important;
            }
            .stApp {
                background-color: #FFF1E0 !important;
            }
            [data-testid="stSidebar"] {
                background-color: #FFE4C7 !important;
            }
            [data-testid="stSidebar"] .css-1d391kg {
                color: black;
            }
            [data-testid="stHeader"] {
                background-color: #FFF1E0 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.sidebar.title("Menu")
        page = st.sidebar.radio("Select Page", ["Input Page", "History Page", "Information Page"])

        st.sidebar.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
        
        st.sidebar.markdown("---")
        logout = st.sidebar.button("\U0001F512 Logout", type="primary")
        if logout:
            st.session_state["start"] = False
            st.session_state["logged_in"] = False
            st.session_state.pop("input_values", None)
            st.rerun()

        st.sidebar.markdown(
            "<div style='text-align: center; font-size: 14px; color: gray;'>2025 © Predict Shop by Team 7</div>",
            unsafe_allow_html=True
        )

        if page == "Input Page":
            input_page()
        elif page == "History Page":
            history_page()
        elif page == "Information Page":
            info_page()

if __name__ == "__main__":
    main()