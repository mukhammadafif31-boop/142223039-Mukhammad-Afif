import streamlit as st
import pandas as pd
import gdown

# ======================
# CONFIG
# ======================
st.set_page_config(page_title="Dashboard Data Drive", layout="wide")

st.title("📊 Dashboard Data Google Drive")
st.markdown("---")

# ======================
# GOOGLE DRIVE FILE
# ======================
file_id = "1z-n2vW1cfp8wYkNkR-aIlDbXJUgQ5C--"
output = "data.csv"

# Download file dari Google Drive
@st.cache_data
def load_data():
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output, quiet=False)

    df = pd.read_csv(output)
    return df

df = load_data()

# ======================
# DASHBOARD
# ======================
st.success("✅ Data berhasil dimuat dari Google Drive!")

# Statistik
col1, col2, col3 = st.columns(3)
col1.metric("Jumlah Baris", df.shape[0])
col2.metric("Jumlah Kolom", df.shape[1])
col3.metric("Missing Value", int(df.isna().sum().sum()))

st.markdown("---")

# Tabel data
st.subheader("📋 Data Lengkap")
st.dataframe(df, use_container_width=True)

# Filter data
st.subheader("🔍 Filter Data")

col_filter = st.selectbox("Pilih kolom:", df.columns)
keyword = st.text_input("Cari data:")

if keyword:
    hasil = df[df[col_filter].astype(str).str.contains(keyword, case=False, na=False)]
    st.write(hasil)

# Download hasil
st.download_button(
    "📥 Download Data CSV",
    df.to_csv(index=False),
    "data.csv",
    "text/csv"
)
