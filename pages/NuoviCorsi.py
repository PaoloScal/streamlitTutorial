import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text
from utils.utils import *

st.markdown("inserimento di nuovi Corsi")


cod = st.text_input("Codice Corso:", placeholder = "CT01")
name = st.text_input("Nome Corso:", placeholder = "Pugilato")
tipo = st.text_input("Tipo del Corso:", placeholder = " ")
lv = st.number_input("Livello del Corso:", placeholder = " ")

if st.button("VAI", type="primary"):
    if (lv >= 1 and lv <= 4 and tipo != '' and name != '' and cod[0] = 'C' and cod[1] = 'T'):
        #CONTROLLA CHE SIA UNICA
        query = f"INSERT INTO Corsi(CodC,Nome,Tipo,Livello) VALUES({cod,name,tipo,lv})"
        st.markdown("Succcesso")
    else:
        st.markdown("Fallimento")
