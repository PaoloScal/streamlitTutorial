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
<<<<<<< HEAD
st.title("Laboratorio di Basi di dati")
st.markdown("Quaderno 4")
st.markdown(":red[Obiettivo]:")
st.markdown("Creare un'applicazione web in Python (Streamlit) in grado di interagire con un database MySQL")
st.markdown("in modo da eseguire interrogazioni in base alle interazioni dell'utente.")
st.markdown("Paolo Scalise")            

if check_connection():
    query = "SELECT OraInizio, COUNT(*) AS NumeroLezioni FROM Programma GROUP BY OraInizio"
    dato = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    st.area_chart(dato,x = "OraInizio")

    query = "SELECT Giorno, COUNT(*) AS NumeroLezioni FROM Programma GROUP BY Giorno"
    dato = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    st.bar_chart(dato,x = "Giorno")
=======
st.sidebar.title("Benvenuto nel sistema gestione hotel")
st.title(":red[Sistema Gestione Hotel]")
if "connection" not in st.session_state.keys():
    st.session_state["connection"]=False

st.header("HOTEL MEGALUSSO 3000")
st.image("images/hotel.png")

check_connection()
>>>>>>> 0110c87403e63d63e8c7d3f18893a127fee74ba7
