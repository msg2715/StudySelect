import streamlit as st
import sqlite3

st.title("회원가입")

id = st.text_input("아이디")
pw = st.text_input("비밀번호", type="password")
pw_check = st.text_input("비밀번호 확인", type="password")
name = st.text_input("이름")
grade = st.text_input("학년")
userclass = st.number_input("반", 1, 10)
number = st.number_input("번호", 1, 31)
mail = st.text_input("학교메일")
# course = st.radio("과정을 선택하세요", ['일반과정', '미술중점'])

btn = st.button("회원가입")

if btn:
    #데이터 베이스 연결
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    
    if pw == pw_check:
        sql = f'''
        INSERT INTO user (userid, userpw, username, usergrade, userclass, usernumber, usermail)
        VALUES ('{id}', '{pw}', '{name}', '{grade}', '{userclass}', '{number}', '{mail}')
        '''
        cursor.execute(sql)
        conn.commit()
        st.success("회원가입 성공!")
    else:
        #회원가입 실패
        st.error("비밀번호가 일치하지 않습니다.")
        
    conn.close()