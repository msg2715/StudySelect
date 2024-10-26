import streamlit as st

st.title("로그인")

id = st.text_input("아이디")
pw = st.text_input("비밀번호", type="password")
btn = st.button("로그인")