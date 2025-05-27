import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text
from utils.utils import *

st.title(":violet[inserimento di nuovi Corsi:]")
def get_list(attributo,tabella):
        query=f"SELECT DISTINCT {attributo} FROM {tabella}"
        result=st.session_state["connection"].execute(text(query))
        result_list=[]
        for row in result.mappings():
            result_list.append(row[attributo])
        return result_list

cod = st.text_input("Codice Corso:", placeholder = "CT01")
name = st.text_input("Nome Corso:", placeholder = "Diventa come Rocky")
tipo = st.text_input("Tipo del Corso:", placeholder = "Pugilato")
lv = st.number_input("Livello del Corso:",min_value=1, max_value=4,step=1)

if st.button("AGGIUNGI", type="primary"):
    if (tipo != '' and name != '' and cod[0] == 'C' and cod[1] == 'T'):
        #CONTROLLA CHE SIA UNICA
        listcod = get_list("CodC","Corsi")
        if (cod not in listcod):
            query = f"INSERT INTO Corsi(CodC,Nome,Tipo,Livello) VALUES{cod,name,tipo,lv}"
            st.session_state["connection"].execute(text(query))
            st.markdown("Operazione effettuata con successo")
        else:
            st.markdown("Il codice è già presente nel database")
    else:
        st.markdown("Impossibie inserire tali dati si prega di riprovare")
query = f"SELECT * FROM Corsi"
dato = st.session_state["connection"].execute(text(query))
df = pd.DataFrame(dato)
st.table(df)