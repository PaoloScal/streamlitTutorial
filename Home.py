import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *


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
st.title(":rainbow[Laboratorio di Basi di dati:]")
st.markdown("Quaderno 4")
st.markdown(":red[Obiettivo]:")
st.markdown("Creare un'applicazione web in Python (Streamlit) in grado di interagire con un database MySQL")
st.markdown("in modo da eseguire interrogazioni in base alle interazioni dell'utente.")
st.markdown("Paolo Scalise")            
col1,col2=st.columns(2)
if check_connection():
    query = "SELECT OraInizio, COUNT(*) AS NumeroLezioni FROM Programma GROUP BY OraInizio"
    dato = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    col1.area_chart(dato,x = "OraInizio")

    query = "SELECT Giorno, COUNT(*) AS NumeroLezioni FROM Programma GROUP BY Giorno"
    dato = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    col2.bar_chart(dato,x = "Giorno")
