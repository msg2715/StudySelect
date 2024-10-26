import streamlit as st

st.title("1학년 수강신청")

###

st.write("선택군1 - 택3")

a_1 = st.checkbox("정치와 법")
a_2 = st.checkbox("세계지리")
a_3 = st.checkbox("윤리와 사상")
a_4 = st.checkbox("세계사")
a_5 = st.checkbox("물리학1")
a_6 = st.checkbox("화학1")
a_7 = st.checkbox("생명과학1")
a_8 = st.checkbox("지구과학1")

###

st.write("선택군2 - 택1")

b_1 = st.checkbox("고전 읽기")
b_2 = st.checkbox("진로 영어")
b_3 = st.checkbox("확률과 통계")
b_4 = st.checkbox("프로그래밍")

###

st.write("선택군3 - 택1")

b_1 = st.checkbox("현대문학 감상")
b_2 = st.checkbox("영어권 문화")
b_3 = st.checkbox("가하")
b_4 = st.checkbox("빅데이터 분석")

###

btn = st.button("저장")