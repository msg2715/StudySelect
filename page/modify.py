import streamlit as st
import sqlite3

if st.session_state.logged_in == False:
    st.error("로그인 후 이용 가능합니다.")
else:
    st.title("회원정보 수정")
    
    pw = st.text_input("비밀번호", type="password")
    pw_check = st.text_input("비밀번호 확인", type="password")
    name = st.text_input("이름")
    grade = st.number_input("학년", 1, 2)
    userclass = st.number_input("반", 1, 10)
    number = st.number_input("번호", 1, 31)
    mail = st.text_input("학교메일")
    
    btn = st.button("회원정보 수정")
    
    if btn:
        if pw == pw_check:
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()

            
            if grade == 1:
                sql = f"UPDATE user SET userpw='{pw}', username='{name}', usergrade={grade}, userclass={userclass}, usernumber={number}, usermail='{mail}', choice='[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]' WHERE userid='{st.session_state.userid}'"
            elif grade == 2:
                sql = f"UPDATE user SET userpw='{pw}', username='{name}', usergrade={grade}, userclass={userclass}, usernumber={number}, usermail='{mail}', choice='[0, 0], [0, 0, 0], [0, 0, 0], [0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0]' WHERE userid='{st.session_state.userid}'"
            
            cursor.execute(sql)
            conn.commit()
            st.success("수정 성공!")
            
            conn.close()
        else:
            st.error("비밀번호가 일치하지 않습니다.")