import streamlit as st
import os
import pandas as pd
from datetime import datetime

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("Agent de Maintenance Prédictive")

uploaded_file = st.file_uploader("1. Télécharger un fichier CSV", type="csv")
df = None

if uploaded_file is not None:
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Fichier sauvegardé : {uploaded_file.name}")
    df = pd.read_csv(save_path)
else:
    saved_files = os.listdir(UPLOAD_DIR)
    if saved_files:
        st.write("Fichiers déjà uploadés :")
        selected_file = st.selectbox("Choisis un fichier", saved_files)
        if selected_file:
            df = pd.read_csv(os.path.join(UPLOAD_DIR, selected_file))
    else:
        st.info("Aucun fichier. Upload un CSV pour commencer.")

if df is not None:
    st.subheader("Aperçu des données")
    st.dataframe(df.head())
    
    if st.button("2. Lancer l'analyse prédictive"):
        max_temp = df['temperature_panneau'].max()
        if max_temp > 75:
            st.error(f"Risque élevé détecté. Température max : {max_temp}°C")
        else:
            st.success("Site Normal")
