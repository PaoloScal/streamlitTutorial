import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text

st.markdown("Agenzie dipsonibili")

query = "SELECT * FROM AGENZIA;"
if st.button("Mostra",type="primary"):
    tab = st.tabs(["Agenzie"])
    df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    with tab:
        st.table(df)