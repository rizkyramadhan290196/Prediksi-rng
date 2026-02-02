import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="RNG Predictor - Rizky", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🎯 RNG PREDICTOR PRO v1.0")
st.write(f"Halo **Rizky**, masukkan data history di bawah ini.")

with st.sidebar:
    st.header("📥 Input Data")
    tgl = st.date_input("Tanggal", datetime.now())
    jam = st.selectbox("Sesi Jam", ["01:00", "07:00", "13:00", "16:00", "19:00", "22:00"])
    angka = st.text_input("Angka 5D")
    if st.button("SIMPAN"):
        if len(angka) == 5:
            st.session_state.history.append({"Tgl": str(tgl), "Jam": jam, "Angka": angka})
            st.success("Tersimpan!")
        else:
            st.error("Harus 5 angka!")

c1, c2 = st.columns(2)
with c1:
    st.subheader("📜 History")
    st.table(pd.DataFrame(st.session_state.history))
with c2:
    st.subheader("🔮 10 Prediksi")
    if st.session_state.history:
        last = int(st.session_state.history[-1]["Angka"])
        for i in range(1, 11):
            res = (last * (i + 7) + random.randint(10, 99)) % 100000
            st.code(f"Urutan {i}: {res:05d}")
