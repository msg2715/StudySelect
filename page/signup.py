import streamlit as st

st.title("회원가입")

id = st.text_input("아이디")
pw = st.text_input("비밀번호", type="password")
pw_check = st.text_input("비밀번호 확인", type="password")
name = st.text_input("이름")
name = st.number_input("반", 1, 10)
name = st.number_input("번호", 1, 31)
mail = st.text_input("학교메일")
course = st.radio("과정을 선택하세요", ['일반과정', '미술중점'])
btn = st.button("회원가입")