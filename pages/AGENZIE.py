import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text
from utils.utils import *

st.title(":red[Agenzie dipsonibili]")
col1,col2,col3=st.columns(3)
if check_connection():
    query = "SELECT COUNT(DISTINCT CodA) AS numAgenzie FROM AGENZIA"
    dato = st.session_state["connection"].execute(text(query))
    col1.metric("Numero Agenzie saltavete:",dato.mappings().first()['numAgenzie'])

    query = "SELECT COUNT(DISTINCT Citta_Indirizzo) AS numCitta FROM AGENZIA"
    dato = st.session_state["connection"].execute(text(query))
    col2.metric("Citta coperte:",dato.mappings().first()['numCitta'])

    query="SELECT Citta_Indirizzo,COUNT(*) AS num FROM AGENZIA GROUP BY Citta_Indirizzo ORDER BY num DESC LIMIT 1;"
    dato = st.session_state["connection"].execute(text(query))
    col3.metric("Citta maggiornmente coperta:",dato.mappings().first()['Citta_Indirizzo'])
    query = "SELECT C.Nome,C.Latitudine AS LAT, C.Longitudine AS LON FROM CITTA C,AGENZIA A WHERE A.Citta_Indirizzo = C.Nome;"
    dato = st.session_state["connection"].execute(text(query))
    df = pd.DataFrame(dato)
    st.map(df)

    supercitta = st.text_input("Citta da ricercare: ", placeholder = "Roma")
    if (supercitta == ''):
        query = "SELECT Citta_indirizzo AS Citta,CONCAT(VIa_indirizzo,' ',Numero_Indirizzo) AS Indirizzo FROM AGENZIA"
    else:
        query = f"SELECT Citta_indirizzo AS Citta,CONCAT(VIa_indirizzo,' ',Numero_Indirizzo) AS Indirizzo FROM AGENZIA WHERE Citta_indirizzo = '{supercitta}'"    
    df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    st.table(df)

st.markdown("Tutte le agenzie presenti nel database:")
if st.button("Mostra",type="primary"):
    tab1,tab2 = st.tabs(["Info Generali","Collocazione geografica"])
    query = "SELECT CodA,Sitoweb,Tel FROM AGENZIA;"
    df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    with tab1:
        st.table(df)
    query = "SELECT CodA,VIa_indirizzo,CAP_Indirizzo,Citta_Indirizzo,Numero_Indirizzo,Stato_Indirizzo FROM AGENZIA;"
    df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    with tab2:
        st.table(df)    