import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text

st.markdown("Andamento Prenotazioni")

if st.button("Mostra",type="primary"):
    query = "SELECT * FROM PRENOTAZIONE"
    df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    st.table(df)