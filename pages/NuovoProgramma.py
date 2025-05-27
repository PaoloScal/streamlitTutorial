import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text
from utils.utils import *
from datetime import *

st.title(":orange[inserimento di nuovi Programmi:]")
def get_list(attributo,tabella):
        query=f"SELECT DISTINCT {attributo} FROM {tabella}"
        result=st.session_state["connection"].execute(text(query))
        result_list=[]
        for row in result.mappings():
            result_list.append(row[attributo])
        return result_list
def find_if_present(attributo1,attributo2,tabella,result1,result2):
        query=f"SELECT DISTINCT {attributo1},{attributo2} FROM {tabella} WHERE {attributo1} = '{result1}' AND {attributo2} = '{result2}'"
        result=st.session_state["connection"].execute(text(query))
        n = 0
        for row in result.mappings():
            n = n+1
        return n


CodFiscList = get_list('CodFisc','Istruttore')
CodFisc= st.selectbox("Seleziona l'istruttore",CodFiscList)
CodCList = get_list("CodC","Corsi")
CodC =  st.selectbox("Seleziona il corso",CodCList)
GiornoList = ["Lundedì","Martedì","Mercoledì","Giovedì","Venerdì"]
Giorno = st.selectbox("Seleziona il giorno",GiornoList)
OraInizio = st.slider("Seleziona l'ora di inizio", time(00,00),time(23,59))
Durata = st.slider("Seleziona la durata", 0,60)
Sala = st.text_input("Sala Scelta:", placeholder = "S1")


if st.button("AGGIUNGI", type="primary"):
    if (CodFisc != '' and Giorno != '' and OraInizio != '' and Durata != '' and Sala != '' and CodC != ''):
        if (find_if_present("CodC","Giorno","Programma",CodC,Giorno) == 0):
            query = f"INSERT INTO Programma(CodFisc,Giorno,OraInizio,Durata,Sala,CodC) VALUES{CodFisc,Giorno,OraInizio.strftime('%HH:%mm'),str(Durata),Sala,CodC}"
            st.session_state["connection"].execute(text(query))
            st.markdown("Operazione effettuata con successo")
        else:
           st.markdown("Un corso simile è gia presente nel database")     
    else:
        st.markdown("Impossibie inserire tali dati si prega di riprovare")
query = f"SELECT * FROM Programma ORDER BY CodC"
dato = st.session_state["connection"].execute(text(query))
df = pd.DataFrame(dato)
st.table(df)