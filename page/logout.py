import streamlit as st

if st.session_state.logged_in == False:
    st.sidebar.write(f"{st.session_state.userid}님 환영합니다.")
    st.error("로그인 후 이용 가능합니다.")
else:
    st.session_state.logged_in = False
    st.session_state.userid = None
    st.session_state.grade = None
    st.success("로그아웃 성공")