import streamlit as st

st.title("2학년 선택과목 정보")


st.write("선택군1")

a_1 = st.expander("정치와 법")
a_1.image("img/정치와법.jpg")

a_2 = st.expander("세계지리")
a_2.image("img/세계지리.jpg")

a_3 = st.expander("윤리와 사상")
a_3.image("img/윤리와사상.jpg")

a_4 = st.expander("세계사")
a_4.image("img/세계사.jpg")

a_5 = st.expander("물리학1")
a_5.image("img/물리학1.jpg")

a_6 = st.expander("화학1")
a_6.image("img/화학1.jpg")

a_7 = st.expander("생명과학1")
a_7.image("img/생명과학1.jpg")

a_8 = st.expander("지구과학1")
a_8.image("img/지구과학1.jpg")


st.write("선택군2")

b_1 = st.expander("고전 읽기")
b_1.image("img/고전읽기.jpg")

b_2 = st.expander("진로 영어")
b_2.image("img/진로영어.jpg")

b_3 = st.expander("확률과 통계")
b_3.image("img/확률과통계.jpg")

b_4 = st.expander("프로그래밍")
b_4.write("프로그래밍") # 이미지가 없어서 글로 적자


st.write("선택군3")

c_1 = st.expander("현대문학 감상")
c_1.image("img/정치와법.jpg") # 추가예정

c_2 = st.expander("영어권 문화")
c_2.image("img/영어권문화.jpg")

c_3 = st.expander("기하")
c_3.image("img/기하.jpg")

c_4 = st.expander("빅데이터 분석")
c_4.image("img/정치와법.jpg") # 추가예정