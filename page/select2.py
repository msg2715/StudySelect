import streamlit as st

st.title("2학년 수강신청")

###

st.write("선택군1 - 택1")

a_1 = st.checkbox("화법과 작문")
a_2 = st.checkbox("언어와 매체")

###

st.write("선택군2 - 택1")

b_1 = st.checkbox("미적분")
b_2 = st.checkbox("수학과제 탐구")
b_3 = st.checkbox("인공지능 수학")

###

st.write("선택군3 - 택1")

c_1 = st.checkbox("심화국어")
c_2 = st.checkbox("심화 영어 독해1")
c_3 = st.checkbox("심화수학1")

###

st.write("선택군4 - 택1")

c_1 = st.checkbox("고전문학 감상")
c_2 = st.checkbox("심화 영어 독해2")
c_3 = st.checkbox("수학적 사고와 적분")
c_4 = st.checkbox("수학적 사고와 통계")

###

st.write("선택군5 - 택3")

a_1 = st.checkbox("생활과 윤리")
a_2 = st.checkbox("한국지리")
a_3 = st.checkbox("동아시아사")
a_4 = st.checkbox("사회·문화")
a_5 = st.checkbox("물리학2")
a_6 = st.checkbox("화학2")
a_7 = st.checkbox("생명과학2")
a_8 = st.checkbox("지구과학2")

###

st.write("선택군6 - 택2")

a_1 = st.checkbox("여행지리")
a_2 = st.checkbox("사회문제 탐구")
a_3 = st.checkbox("고전과 윤리")
a_4 = st.checkbox("생활과 과학")
a_5 = st.checkbox("융합과학")
a_6 = st.checkbox("자료구조")

###

st.write("선택군7 - 택1")

a_1 = st.checkbox("중국어")
a_2 = st.checkbox("일본어")

###

btn = st.button("저장")