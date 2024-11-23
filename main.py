import streamlit as st

# 세션 설정
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.userid = None
    st.session_state.grade = None


# 타이틀 설정
st.set_page_config(
    page_title = "매천고 수강신청",
    page_icon = "😎"
)


# 페이지 설정
pages = {
    "로그인/회원가입" : [
        st.Page("page/login.py", title="로그인"),
        st.Page("page/signup.py", title="회원가입"),
        st.Page("page/modify.py", title="회원정보수정"),
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
    ],
    "회원탈퇴" : [
        st.Page("page/account_deletion.py", title="회원탈퇴"),
    ]
}

pg = st.navigation(pages)
pg.run()


# 사이드바 설정
if st.session_state.logged_in == True:
    st.sidebar.write(f"{st.session_state.userid}님 환영합니다.")
else:
    st.sidebar.write("로그인이 되어있지 않습니다.")