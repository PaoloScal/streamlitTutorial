import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine,text
from utils.utils import *

st.title(":red[Stanze dipsonibili]")
st.markdown("Tutte le stanze prendenti nel database")

if check_connection():
    def get_list(attributo,tabella):
        query=f"SELECT DISTINCT {attributo} FROM {tabella}"
        result=st.session_state["connection"].execute(text(query))
        result_list=[]
        for row in result.mappings():
            result_list.append(row[attributo])
        return result_list

    def map_optional(optional):
        query=""
        for element in optional:
            query=query+(f" AND HAS_OPTIONAL.OPTIONAL_Optional='{element}'")
        return query

    tipo_stanza = st.selectbox("Di che tipo di stanza hai bisogno?",["Singola","Doppia","Tripla","Tutte"])
    if (tipo_stanza == "Tutte" or tipo_stanza == ''):
        typestanza = ''
    else:
        typestanza = f"AND STANZA.Type = '{tipo_stanza}'"

    optionalList=get_list("OPTIONAL_Optional","HAS_OPTIONAL")
    option = st.multiselect("Seleziona gli optional desiderati:",optionalList)
    optionalq = map_optional(option)

    if st.checkbox("Voglio la cucina"):
         cucinaFlag = True
    else:
         cucinaFlag = False

    if cucinaFlag:
        query=f"""SELECT CodS,Piano,Superficie,Type,HAS_OPTIONAL.OPTIONAL_Optional AS Optional
            FROM `STANZA`, `HAS_OPTIONAL`,`HAS_SPAZI`
            WHERE CodS=HAS_OPTIONAL.STANZA_CodS AND CodS=HAS_SPAZI.STANZA_CodS {typestanza} {optionalq} AND HAS_SPAZI.SPAZI_Spazi='cucina'             """
    else:
        query=f"""SELECT CodS,Piano,Superficie,Type,HAS_OPTIONAL.OPTIONAL_Optional AS Optional
            FROM `STANZA`, `HAS_OPTIONAL`
            WHERE CodS=HAS_OPTIONAL.STANZA_CodS {typestanza} {optionalq}
            """       
 
            
    df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
    st.table(df)
    
    with st.expander("Stanze"):
            if cucinaFlag:
                query=f"""SELECT DISTINCT CodS,Piano,Type
                FROM `STANZA`, `HAS_OPTIONAL`,`HAS_SPAZI`
                WHERE CodS=HAS_OPTIONAL.STANZA_CodS AND CodS=HAS_SPAZI.STANZA_CodS {typestanza} {optionalq} AND HAS_SPAZI.SPAZI_Spazi='cucina' 
                GROUP BY CodS
                """
            else:
                query=f"""SELECT DISTINCT CodS,Piano,Type
                    FROM `STANZA`, `HAS_OPTIONAL`
                    WHERE CodS=HAS_OPTIONAL.STANZA_CodS {typestanza} {optionalq}
                    GROUP BY CodS
                    LIMIT 5;
                    """
            df = pd.DataFrame(st.session_state["connection"].execute(text(query)))
            
            for index, row in df.iterrows():
                col1,col2=st.columns(2)
                col1.subheader(f":red[Stanza {index+1}]")
                col1.text(f"Codice Stanza: {row['CodS']}")
                col1.text(f"Piano: {row['Piano']}")
                col1.text(f"Tipo: {row['Type']}")
                col2.image(f"images/{row['Type']}.png")


