import streamlit as st

pages = {
    "로그인/회원가입" : [
        st.Page("page/login.py", title="로그인"),
        st.Page("page/signup.py", title="회원가입"),
        st.Page("page/logout.py", title="로그아웃")
    ],
    "선택과목정보" : [
        st.Page("page/information1.py", title="2학년 선택과목 정보"),
        st.Page("page/information2.py", title="3학년 선택과목 정보")
    ],
    "수강신청" : [
        st.Page("page/select1.py", title="1학년 수강신청"),
        st.Page("page/select2.py", title="2학년 수강신청")
    ],
    "통계/분석" : [
        st.Page("page/statistics.py", title="선택과목 신청현황 및 분석"),
    ]
}


pg = st.navigation(pages)
pg.run()