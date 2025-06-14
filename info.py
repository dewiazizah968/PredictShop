import streamlit as st
import pandas as pd
import base64
from io import BytesIO
from PIL import Image

def info_page():
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
            <div class="header-title">Information</div>
        </div>
    """, unsafe_allow_html=True)

    # Tabel fitur input
    data = {
        "Fitur": [
            "Administrative", 
            "Administrative Duration", 
            "Informational", 
            "Informational Duration", 
            "Product Related", 
            "Product Related Duration",
            "Bounce Rates", 
            "Exit Rates", 
            "Page Values", 
            "Special Day", 
            "Browser", 
            "Weekend", 
            "Month", 
            "Visitor Type"
        ],
        "Keterangan": [
            "Jumlah halaman administratif yang dikunjungi pengguna",
            "Durasi waktu yang dihabiskan di halaman administratif",
            "Jumlah halaman informasional yang dikunjungi pengguna",
            "Durasi waktu yang dihabiskan di halaman informasional",
            "Jumlah halaman produk yang dikunjungi pengguna",
            "Durasi waktu yang dihabiskan di halaman produk",
            "Persentase pengguna keluar setelah melihat satu halaman",
            "Persentase pengguna keluar dari halaman tertentu",
            "Nilai halaman yang dikunjungi (konversi)",
            "Menunjukkan kedekatan waktu dengan hari istimewa (misalnya liburan)",
            "Jenis browser yang digunakan pengguna",
            "Apakah kunjungan dilakukan di akhir pekan",
            "Bulan saat kunjungan terjadi",
            "Tipe pengunjung (baru atau kembali)"
        ]
    }

    df_info = pd.DataFrame(data)
    st.subheader("Fitur Input")
    st.dataframe(df_info, use_container_width=True)

    # Tabel hasil prediksi
    forecast_data = {
        "Keterangan": ["Will Buy", "Won't Buy"],
        "Arti": [
            "Pengunjung kemungkinan besar akan melakukan pembelian berdasarkan perilaku mereka di situs.",
            "Pengunjung kemungkinan besar tidak akan melakukan pembelian meskipun telah mengunjungi situs."
        ]
    }

    df_forecast = pd.DataFrame(forecast_data)
    st.subheader("Forecast Result")
    st.dataframe(df_forecast, use_container_width=True)