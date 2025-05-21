import streamlit as st
import numpy as np
import pandas as pd
from utils.utils import *


st.set_page_config(
    page_title="La mia App",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://dbdmg.polito.it/',
        'Report a bug': "https://dbdmg.polito.it/",
        'About': "# Corso di *Basi di Dati*"
    }
)
st.sidebar.title("Benvenuto nel sistema gestione hotel")
st.title(":red[Sistema Gestione Hotel]")
if "connection" not in st.session_state.keys():
    st.session_state["connection"]=False

st.header("HOTEL MEGALUSSO 3000")
st.image("images/hotel.png")

check_connection()