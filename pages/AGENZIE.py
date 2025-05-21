import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text

st.title(":red[Agenzie dipsonibili]")

query = "SELECT COUNT(DISTINCT CodA) AS numAgenzie FROM AGENZIA"
dato = pd.DataFrame(st.session_state["connection"].execute(text(query)))
st.metric("Numero Agenzie saltavete:",dato.mappings().first()['numAgenzie'])
#st.metric("Citta coperte:",0)
#st.metric("Citta maggiornmente coperta:",0)



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