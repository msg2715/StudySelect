import streamlit as st
import sqlite3

if st.session_state.logged_in == False:
    st.sidebar.write(f"{st.session_state.userid}님 환영합니다.")
    st.error("로그인 후 이용 가능합니다.")
else:
    st.title("회원탈퇴")
    
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("회원탈퇴")
    
    if btn:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM user WHERE userid='{st.session_state.userid}'")
        row = cursor.fetchone()
        
        db_pw = row[1]
        
        if pw == db_pw:
            cursor.execute(f"DELETE FROM user WHERE userid = '{st.session_state.userid}'")
            conn.commit()
            st.session_state.logged_in = False
            st.session_state.userid = None
            st.session_state.grade = None
            st.success("회원탈퇴 성공")
        else:
            st.error("아이디 또는 비밀번호가 틀렸습니다.")
            
        conn.close()