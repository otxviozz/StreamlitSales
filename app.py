import streamlit as st
import mysql as sql
from src.auth.signin import login_verification

st.title("Login - Mercadinho Jucrisc")

username = st.text_input("Digite o nome de usuário")
password = st.text_input("Digite a senha", type="password")
submit = st.button("Logar")

if submit:
    user_type= login_verification(username, password)

    if user_type == "management":
        st.write("Login efetuado! Gerência")
    elif user_type == "seller":
        st.write("Login efetuado! Vendedor")
    else:
        st.write(user_type)