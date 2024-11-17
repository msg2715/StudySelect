import streamlit as st
import sqlite3

if st.session_state.logged_in == True:
    st.error("이미 로그인이 되어있습니다.")
else:
    st.title("로그인")

    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("로그인")

    if btn:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM user WHERE userid='{id}'") # user 테이블에서 userid = id인 데이터 찾기
        row = cursor.fetchone()
        
        if row:
            db_id = row[0]
            db_pw = row[1]
        else:
            db_id = ''
            db_pw = ''
            
        if db_pw == pw:
            # 로그인 성공
            st.session_state.logged_in = True
            st.session_state.userid = id
            st.session_state.grade = row[3]
        else:
            # 로그인 실패
            st.error("로그인 실패!!")