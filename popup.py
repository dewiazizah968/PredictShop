import streamlit as st
import base64

def show_popup(prediction: bool):
    if not st.session_state.get("show_modal", False):
        return

    image_path = "assets/buy.png" if prediction else "assets/notbuy.png"
    label = "WILL BUY 🛒" if prediction else "WON'T BUY ❌"
    overlay_color = "#55CF79" if prediction else "#E87170"

    with open(image_path, "rb") as f:
        img_bytes = f.read()
    img_base64 = base64.b64encode(img_bytes).decode()

    modal_html = f"""
    <style>
    .modal-background {{
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        background-color: rgba(0,0,0,0.6);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9998;
    }}
    .modal-content {{
        background-color: {overlay_color};
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        width: 500px;
        height: 400px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        position: relative;
        z-index: 9999;
    }}
    .modal-content h3 {{
        margin-top: 0;
    }}

    /* Styling untuk tombol OK agar muncul di modal */
    .stButton button {{
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        z-index: 10000;
        background-color: #FFA500;
        color: white;
        border: none;
        border-radius: 5px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }}

    .stButton button:hover {{
        background-color: #e69500;
        color: black;
        cursor: pointer;
    }}

    .stButton button:active {{
        color: white;
    }}
    </style>

    <div class="modal-background" id="customModal">
        <div class="modal-content">
            <h3>🎯 PREDICTION RESULT</h3>
            <img src="data:image/png;base64,{img_base64}" width="150"><br>
            <strong style="font-size: 1.2rem;">{label}</strong><br><br>
            <!-- Tombol OK streamlit akan muncul di sini -->
        </div>
    </div>
    """

    st.markdown(modal_html, unsafe_allow_html=True)

    if st.button("OK"):
        st.session_state["show_modal"] = False
        st.experimental_rerun()
