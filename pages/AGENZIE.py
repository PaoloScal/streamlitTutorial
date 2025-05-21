import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text

st.title(":red[Agenzie dipsonibili]")

query = "SELECT COUNT(DISTINCT CodA) AS numAgenzie FROM AGENZIA"
dato = st.session_state["connection"].execute(text(query))
st.metric("Numero Agenzie saltavete:",dato.mappings().first()['numAgenzie'])

query = "SELECT COUNT(DISTINCT Citta_Indirizzo) AS numCitta FROM AGENZIA"
dato = st.session_state["connection"].execute(text(query))
st.metric("Citta coperte:",dato.mappings().first()['numCitta'])

query = "SELECT COUNT(DISTINCT CodA) AS numAgenzie FROM AGENZIA"
dato = st.session_state["connection"].execute(text(query))
st.metric("Citta maggiornmente coperta:",dato.mappings().first()['bestCitta'])



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