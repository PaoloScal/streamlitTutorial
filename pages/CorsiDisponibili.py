import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text
from utils.utils import *

st.subheader("Filtraggio Corsi")
col1,col2=st.columns(2)
if check_connection():
    def get_list(attributo,tabella):
        query=f"SELECT DISTINCT {attributo} FROM {tabella}"
        result=st.session_state["connection"].execute(text(query))
        result_list=[]
        for row in result.mappings():
            result_list.append(row[attributo])
        return result_list


    



    query = "SELECT COUNT(DISTINCT CodC) AS Num FROM Corsi "
    dato = st.session_state["connection"].execute(text(query))
    col1.metric("Numero Corsi Disponibili:",dato.mappings().first()['Num'])

    query = "SELECT COUNT(DISTINCT Tipo) AS Num FROM Corsi "
    dato = st.session_state["connection"].execute(text(query))
    col2.metric("Numero Di Tipi di Corso Differenti:",dato.mappings().first()['Num'])
    
    tipoList = get_list('Tipo','Corsi')
    tipo= st.selectbox("Di che tipo di corso hai bisogno?",tipoList)
    if (tipo == ''):
        typestr= ''
    else:
        typestr = f"AND Corsi.Tipo = '{tipo}'"

    LivelloList = get_list('Livello','Corsi')
    liv= st.selectbox("A che livello di allenamento sei interessato?",LivelloList)
    if (liv == ''):
        livstr= ''
    else:
        livstr = f"AND Corsi.Livello = '{liv}'"    
     

    query = f"SELECT Programma.Giorno,Programma.OraInizio,Programma.Durata,Programma.Sala,CONCAT(Istruttore.Nome,' ',Istruttore.Cognome) AS NomeCognome,Istruttore.Email FROM Corsi,Istruttore,Programma WHERE Corsi.CodC = Programma.CodC  AND Programma.CodFisc = Istruttore.CodFisc {typestr} {livstr}"
    dato = st.session_state["connection"].execute(text(query))
    df = pd.DataFrame(dato)
    if (dato == ''):
        st.markdown("errore")
    else:
        st.table(df)