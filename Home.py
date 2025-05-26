import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Quaderno 4",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://dbdmg.polito.it/',
        'Report a bug': "https://dbdmg.polito.it/",
        'About': "# Corso di *Basi di Dati*"
    }
)
st.title("Laboratorio di Basi di dati")
st.markdown("Quaderno 4")
st.markdown(":red[Obiettivo]:")
st.markdown("Creare un'applicazione web in Python (Streamlit) in grado di interagire con un database MySQL")
st.markdown("in modo da eseguire interrogazioni in base alle interazioni dell'utente.")
st.markdown("Paolo Scalise")            