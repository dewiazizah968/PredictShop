import streamlit as st
import pandas as pd
import numpy as np
import joblib
import random
import os
from popup import show_popup
from PIL import Image
import base64
from io import BytesIO

if "show_modal" not in st.session_state:
    st.session_state["show_modal"] = False

def input_page():
    st.markdown("""
        <style>
        /* Target field input angka */
        input[type="number"] {
            background-color: white !important;
            color: black !important;
            border: none !important;
            border-radius: 4px !important;
        }
                
        /* Tombol + dan - */
        .stNumberInput button {
            background-color: white !important;
            color: black !important;
            border: none !important;
            border-radius: none !important;
        }

        /* Dropdown */
        .stSelectbox > div > div {
            background-color: white !important;
            color: black !important;
        }

        /* Target Button Prediksi */
        button[kind="secondaryFormSubmit"] {
            background-color: #FFA500 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: bold;
        }

        /* Hover efek Prediksi */
        button[kind="secondaryFormSubmit"]:hover {
            background-color: #e69500 !important;
            color: black !important;
        }

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
            <div class="header-title">Predict Shop</div>
        </div>
    """, unsafe_allow_html=True)

    # Load model
    model = joblib.load("svm_manual_model.pkl")
    w_akhir = model['weights']
    b_akhir = model['bias']
    scaler = model['scaler']
    selected_features = model['features']

    def set_default_input():
        st.session_state.input_values = {
            'Administrative': 0,
            'Administrative_Duration': 0.0,
            'Informational': 0,
            'Informational_Duration': 0.0,
            'ProductRelated': 0,
            'ProductRelated_Duration': 0.0,
            'BounceRates': 0.0,
            'ExitRates': 0.0,
            'PageValues': 0.0,
            'SpecialDay': 0.0,
            'Browser': 0,
            'Weekend': "No",
            'Month': 'Dec',
            'VisitorType': 'New_Visitor'
        }

    if 'input_values' not in st.session_state:
        set_default_input()

    with st.form("form_input"):
        col1, col2, col3 = st.columns([1, 1, 1])  
        with col1:
            st.session_state.input_values['Administrative'] = st.number_input(
                "Administrative", min_value=0, step=1, value=st.session_state.input_values['Administrative'])
            st.session_state.input_values['Administrative_Duration'] = st.number_input(
                "Administrative Duration", min_value=0.0, value=st.session_state.input_values['Administrative_Duration'])
            st.session_state.input_values['Informational'] = st.number_input(
                "Informational", min_value=0, step=1, value=st.session_state.input_values['Informational'])
            st.session_state.input_values['Informational_Duration'] = st.number_input(
                "Informational Duration", min_value=0.0, value=st.session_state.input_values['Informational_Duration'])
            st.session_state.input_values['ProductRelated'] = st.number_input(
                "Product Related", min_value=0, step=1, value=st.session_state.input_values['ProductRelated'])

        with col2:
            st.session_state.input_values['ProductRelated_Duration'] = st.number_input(
                "Product Related Duration", min_value=0.0, value=st.session_state.input_values['ProductRelated_Duration'])
            st.session_state.input_values['BounceRates'] = st.slider(
                "Bounce Rates", 0.0, 1.0, value=st.session_state.input_values['BounceRates'])
            st.session_state.input_values['ExitRates'] = st.number_input(
                "Exit Rates (0-1)", min_value=0.0, max_value=1.0, format="%.6f", value=st.session_state.input_values['ExitRates'])
            st.session_state.input_values['PageValues'] = st.number_input(
                "Page Values", min_value=0.0, format="%.6f", value=st.session_state.input_values['PageValues'])
            st.session_state.input_values['SpecialDay'] = st.slider(
                "Special Day", 0.0, 1.0, value=st.session_state.input_values['SpecialDay'])

        with col3:
            st.session_state.input_values['Browser'] = st.number_input(
                "Browser", min_value=0, step=1, value=st.session_state.input_values['Browser'])
            st.session_state.input_values['Weekend'] = st.radio(
                "Weekend?", ["Yes", "No"], index=0 if st.session_state.input_values['Weekend'] == "Yes" else 1)
            st.session_state.input_values['Month'] = st.selectbox(
                "Month", ['Dec', 'Feb', 'Mar', 'May', 'Nov', 'Oct'],
                index=['Dec', 'Feb', 'Mar', 'May', 'Nov', 'Oct'].index(st.session_state.input_values['Month']))
            st.session_state.input_values['VisitorType'] = st.selectbox(
                "Visitor Type", ['New_Visitor', 'Returning_Visitor'],
                index=0 if st.session_state.input_values['VisitorType'] == "New_Visitor" else 1)

        col_left, col_center, col_right = st.columns([1, 2, 1])
        with col_center:
            generate = st.form_submit_button("Generate Random Data", use_container_width=True)

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        col_spacer, col_submit = st.columns([5, 1])
        with col_submit:
            submitted = st.form_submit_button("Prediksi", use_container_width=True)

    # Generate random input
    if generate:
        st.session_state.input_values = {
            'Administrative': random.randint(0, 30),
            'Administrative_Duration': round(random.uniform(0, 3400), 2),
            'Informational': random.randint(0, 30),
            'Informational_Duration': round(random.uniform(0, 2550), 2),
            'ProductRelated': random.randint(0, 800),
            'ProductRelated_Duration': round(random.uniform(0, 64000), 2),
            'BounceRates': round(random.uniform(0.0, 1.0), 2),
            'ExitRates': round(random.uniform(0.0, 1.0), 6),
            'PageValues': round(random.uniform(0.0, 362), 6),
            'SpecialDay': round(random.uniform(0.0, 1.0), 2),
            'Browser': random.randint(1, 13),
            'Weekend': random.choice(["Yes", "No"]),
            'Month': random.choice(['Dec', 'Feb', 'Mar', 'May', 'Nov', 'Oct']),
            'VisitorType': random.choice(['New_Visitor', 'Returning_Visitor'])
        }
        st.rerun()  

    # Prediksi
    if submitted:
        iv = st.session_state.input_values
        data_user = {
            'Administrative': iv['Administrative'],
            'Administrative_Duration': iv['Administrative_Duration'],
            'Informational': iv['Informational'],
            'Informational_Duration': iv['Informational_Duration'],
            'ProductRelated': iv['ProductRelated'],
            'ProductRelated_Duration': iv['ProductRelated_Duration'],
            'BounceRates': iv['BounceRates'],
            'ExitRates': iv['ExitRates'],
            'PageValues': iv['PageValues'],
            'SpecialDay': iv['SpecialDay'],
            'Browser': iv['Browser'],
            'Weekend': iv['Weekend'].lower() == "yes",
            'Month': iv['Month'],
            'VisitorType': iv['VisitorType']
        }

        df = pd.DataFrame([data_user])
        df['Weekend'] = int(df['Weekend'].iloc[0])

        # One-hot encoding
        for m in ['Dec', 'Feb', 'Mar', 'May', 'Nov', 'Oct']:
            df[f'Month_{m}'] = 1 if df['Month'].iloc[0] == m else 0
        df['VisitorType_New_Visitor'] = 1 if df['VisitorType'].iloc[0] == 'New_Visitor' else 0
        df['VisitorType_Returning_Visitor'] = 1 if df['VisitorType'].iloc[0] == 'Returning_Visitor' else 0
        df = df.drop(columns=['Month', 'VisitorType'])

        for col in selected_features:
            if col not in df:
                df[col] = 0
        df = df[selected_features]

        # Scaling
        scaled_input = scaler.transform(df)

        # Prediksi manual SVM
        hasil_pred = np.dot(scaled_input, w_akhir) + b_akhir
        hasil = int(hasil_pred >= 0)

        # Popup
        st.session_state["show_modal"] = True
        show_popup(hasil == 1)

        id_user = str(random.randint(10000, 99999))

        save_data = {
            'ID_User': id_user,
            **iv,
            'Prediksi': 'Membeli' if hasil == 1 else 'Tidak Membeli'
        }

        save_df = pd.DataFrame([save_data])

        file_path = "history_prediksi.csv"

        if os.path.exists(file_path):
            existing_df = pd.read_csv(file_path)
            save_df.insert(0, 'No', len(existing_df) + 1)
            save_df = pd.concat([existing_df, save_df], ignore_index=True)
        else:
            save_df.insert(0, 'No', 1)

        save_df.to_csv(file_path, index=False)
