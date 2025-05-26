import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text
from utils.utils import *

st.subheader("Filtraggio Corsi")
col1,col2=st.columns(2)
if check_connection():
    
    Cognome = st.text_input("Cognome dell'istruttore:", placeholder = "Rossi")
    if (Cognome == ''):
        Cognomestr= ''
    else:
        Cognomestr = f"AND Istruttore.Cognome = '{Cognome}'"

    query="SELECT MIN(DataNascita), MAX(DataNascita) FROM Istruttore"
    date=st.session_state["connection"].execute(text(query))
    min_max=[dict(zip(date.keys(), result)) for result in date]

    #sappiamo che ci viene restituita una sola tupla
    min_value=min_max[0]['MIN(DataNascita)']
    max_value=min_max[0]['MAX(DataNascita)']
    #specificare min_value e max_value per impostare il widget con il range di date
    date_range=st.date_input("Seleziona il range di date:",value=(min_value,max_value),min_value=min_value,max_value=max_value)
     
    query = f"SELECT * FROM Istruttore WHERE DataNascita >'{date_range[0]}' AND DataNascita <'{date_range[1]}' {Cognomestr}"
    dato = st.session_state["connection"].execute(text(query))
    df = pd.DataFrame(dato)
    if (dato == ''):
        st.markdown("errore")
    else:
        for index, row in df.iterrows():
                col1,col2,col3,col4,col5,col6=st.columns(6)
                col1.subheader(f":red[Instruttore {index+1}]")
                col2.text(f"Nome: {row['Nome']}")
                col3.text(f"Cognome: {row['Cognome']}")
                col4.text(f"DataNascita: {row['DataNascita']}")
                col5.text(f"Email: {row['Email']}")
                col6.text(f"Telefono: {row['Telefono']}")
                