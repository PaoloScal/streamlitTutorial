import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text
from utils.utils import *

st.title(":red[Andamento Prenotazioni]")
st.markdown("Le prenotazioni effettuate fino ad ora:")
if check_connection():
    if st.button("Mostra",type="primary"):
        query = "SELECT * FROM PRENOTAZIONE"
        df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
        st.table(df)