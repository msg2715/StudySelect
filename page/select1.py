import streamlit as st
import sqlite3

if st.session_state.logged_in == False:
    st.error("로그인 후 이용 가능합니다.")
elif st.session_state.grade != 1:
    st.error("해당 학년이 아닙니다.")
else:
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

    c_1 = st.checkbox("현대문학 감상")
    c_2 = st.checkbox("영어권 문화")
    c_3 = st.checkbox("기하")
    c_4 = st.checkbox("빅데이터 분석")

    ###

    btn = st.button("저장")
    
    
    if btn:
        a = list(map(int, [a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8]))
        b = list(map(int, [b_1, b_2, b_3, b_4]))
        c = list(map(int, [c_1, c_2, c_3, c_4]))
        
        print(a, b, c)
        
        if sum(a) != 3:
            st.error("선택군1에서 3개의 과목을 골라주세요.")
        elif sum(b) != 1:
            st.error("선택군2에서 1개의 과목을 골라주세요.")
        elif sum(c) != 1:
            st.error("선택군3에서 1개의 과목을 골라주세요.")
        else:
            # 저장
            conn = sqlite3.connect('db.db')
            cursor = conn.cursor()

            # 선택과목 수정
            cursor.execute(f"UPDATE user SET choice = '{[a, b, c]}' WHERE userid='{st.session_state.userid}'")
            
            conn.commit()
            conn.close()
            
            st.success("저장이 완료되었습니다!")
            
            


