import streamlit as st
from sqlalchemy import create_engine,text


#connettersi all'engine
def connect_db(dialect,username,password,host,dbname):
    try:
        engine=create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}')
        conn=engine.connect()
        return conn
    except:
        return False



#Controllare se la connessione al db è stata effettuata
def check_connection():
    if "connection" not in st.session_state.keys():
        st.session_state["connection"]=False

    if st.sidebar.button("Connettiti al Database"):
<<<<<<< HEAD
        myconnection=connect_db(dialect="mysql+pymysql",username="root",password="mypassword",host="localhost",dbname="palestra")
=======
        myconnection=connect_db(dialect="mysql+pymysql",username="root",password="mypassword",host="localhost",dbname="hotel")
>>>>>>> 0110c87403e63d63e8c7d3f18893a127fee74ba7
        if myconnection is not False:
            st.session_state["connection"]=myconnection

        else:
            st.session_state["connection"]=False
            st.sidebar.error("Errore nella connessione al DB")

    if st.session_state["connection"]:
        st.sidebar.success("Connesso al DB")
<<<<<<< HEAD
        return True
=======
        return True
>>>>>>> 0110c87403e63d63e8c7d3f18893a127fee74ba7
