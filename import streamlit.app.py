import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Data Drive", layout="wide")

st.title("📊 Dashboard Data dari Google Drive")
st.markdown("---")

# =========================
# LINK GOOGLE DRIVE FILE
# =========================
file_id = "1z-n2vW1cfp8wYkNkR-aIlDbXJUgQ5C--"
url = f"https://drive.google.com/uc?id={file_id}"

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    try:
        # Jika file CSV
        df = pd.read_csv(url)
        return df
    except:
        return None

df = load_data()

# =========================
# TAMPILAN UTAMA
# =========================
if df is not None:
    st.success("✅ Data berhasil diambil dari Google Drive!")

    # Statistik ringkas
    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah Baris", df.shape[0])
    col2.metric("Jumlah Kolom", df.shape[1])
    col3.metric("Missing Value", df.isna().sum().sum())

    st.markdown("---")

    # Tabel data
    st.subheader("📋 Data Lengkap")
    st.dataframe(df, use_container_width=True)

    # Filter sederhana
    st.subheader("🔍 Filter Data")
    kolom = st.selectbox("Pilih kolom untuk filter:", df.columns)
    nilai = st.text_input("Masukkan kata kunci:")

    if nilai:
        hasil = df[df[kolom].astype(str).str.contains(nilai, case=False, na=False)]
        st.write(hasil)

else:
    st.error("❌ Gagal membaca data. Pastikan file Google Drive adalah CSV dan public.")
