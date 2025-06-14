import streamlit as st
import pandas as pd

def history_page():
    st.markdown("""
        <style>
            .header-container {
                display: flex;
                align-items: center;
                gap: 20px;
                margin-bottom: 30px;
            }
            .header-title {
                font-size: 50px;
                font-weight: bold;
                padding-top: 10px;
            }
            .header-logo {
                width: 100px;
            }
        </style>
    """, unsafe_allow_html=True)

    import base64
    from io import BytesIO
    from PIL import Image

    def get_image_base64(path):
        img = Image.open(path)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        img_b64 = base64.b64encode(img_bytes).decode()
        return img_b64

    logo_base64 = get_image_base64("assets/logo.png")

    st.markdown(f"""
        <div class="header-container">
            <img src="data:image/png;base64,{logo_base64}" class="header-logo">
            <div class="header-title">History</div>
        </div>
    """, unsafe_allow_html=True)

    try:
        df = pd.read_csv("history_prediksi.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.error("File 'history_prediksi.csv' tidak ditemukan.")
