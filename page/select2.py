import streamlit as st
import sqlite3

if st.session_state.logged_in == False:
    st.error("로그인 후 이용 가능합니다.")
elif st.session_state.grade != 2:
    st.error("해당 학년이 아닙니다.")
else:
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

    d_1 = st.checkbox("고전문학 감상")
    d_2 = st.checkbox("심화 영어 독해2")
    d_3 = st.checkbox("수학적 사고와 적분")
    d_4 = st.checkbox("수학적 사고와 통계")

    ###

    st.write("선택군5 - 택2")

    e_1 = st.checkbox("생활과 윤리")
    e_2 = st.checkbox("한국지리")
    e_3 = st.checkbox("동아시아사")
    e_4 = st.checkbox("사회·문화")
    e_5 = st.checkbox("물리학2")
    e_6 = st.checkbox("화학2")
    e_7 = st.checkbox("생명과학2")
    e_8 = st.checkbox("지구과학2")

    ###

    st.write("선택군6 - 택2")

    f_1 = st.checkbox("여행지리")
    f_2 = st.checkbox("사회문제 탐구")
    f_3 = st.checkbox("고전과 윤리")
    f_4 = st.checkbox("생활과 과학")
    f_5 = st.checkbox("융합과학")
    f_6 = st.checkbox("자료구조")

    ###

    st.write("선택군7 - 택1")

    g_1 = st.checkbox("중국어")
    g_2 = st.checkbox("일본어")

    ###

    btn = st.button("저장")
    
    
    if btn:
        a = list(map(int, [a_1, a_2]))
        b = list(map(int, [b_1, b_2, b_3]))
        c = list(map(int, [c_1, c_2, c_3]))
        d = list(map(int, [d_1, d_2, d_3, d_4]))
        e = list(map(int, [e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8]))
        f = list(map(int, [f_1, f_2, f_3, f_4, f_5, f_6]))
        g = list(map(int, [g_1, g_2]))
        
        if sum(a) != 1:
            st.error("선택군1에서 1개의 과목을 골라주세요.")
        elif sum(b) != 1:
            st.error("선택군2에서 1개의 과목을 골라주세요.")
        elif sum(c) != 1:
            st.error("선택군3에서 1개의 과목을 골라주세요.")
        elif sum(d) != 1:
            st.error("선택군4에서 1개의 과목을 골라주세요.")
        elif sum(e) != 2:
            st.error("선택군5에서 2개의 과목을 골라주세요.")
        elif sum(f) != 2:
            st.error("선택군6에서 2개의 과목을 골라주세요.")
        elif sum(g) != 1:
            st.error("선택군7에서 1개의 과목을 골라주세요.")
        else:
            # 저장
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()

            # 선택과목 수정
            cursor.execute(f"UPDATE user SET choice = '{[a, b, c, d, e, f, g]}' WHERE userid='{st.session_state.userid}'")
            
            conn.commit()
            conn.close()
            
            st.success("저장이 완료되었습니다!")