import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text
from utils.utils import *

tipo_stanza = st.radio("Di che tipo di stanza hai bisogno?")

option = st.selectbox("Seleziona gli optional desiderati:",())


if st.checkbox("Voglio la cucina"):





st.title(":red[Stanze dipsonibili]")
st.markdown("Tutte le stanze prendenti nel database")
if check_connection():
    if st.button("Mostra",type="primary"):
        query = "SELECT * FROM STANZA"
        df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
        st.table(df)