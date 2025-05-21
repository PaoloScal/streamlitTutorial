import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text

st.title(":red[Stanze dipsonibili]")
st.markdown("Tutte le stanze prendenti nel database")

if st.button("Mostra",type="primary"):
    query = "SELECT * FROM STANZA"
    df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    st.table(df)