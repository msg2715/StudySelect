import streamlit as st
import plotly.express as px
import sqlite3
import numpy as np

conn = sqlite3.connect('db.db')
cursor = conn.cursor()


# 2학년 선택과목 데이터 시각화
cursor.execute(f"SELECT choice FROM user WHERE usergrade=1")
row = cursor.fetchall()

result_1 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in row:
    choice = eval(i[0])
    
    result_1[0] = np.array(result_1[0]) + np.array(choice[0])
    result_1[1] = np.array(result_1[1]) + np.array(choice[1])
    result_1[2] = np.array(result_1[2]) + np.array(choice[2])

for i in range(0, 3):
        result_1[i] = result_1[i].tolist()


# 3학년 선택과목 데이터 시각화
cursor.execute(f"SELECT choice FROM user WHERE usergrade=2")
row = cursor.fetchall()

result_2 = [[0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0]]

for i in row:
    choice = eval(i[0])
    
    result_2[0] = np.array(result_2[0]) + np.array(choice[0])
    result_2[1] = np.array(result_2[1]) + np.array(choice[1])
    result_2[2] = np.array(result_2[2]) + np.array(choice[2])
    result_2[3] = np.array(result_2[3]) + np.array(choice[3])
    result_2[4] = np.array(result_2[4]) + np.array(choice[4])
    result_2[5] = np.array(result_2[5]) + np.array(choice[5])
    result_2[6] = np.array(result_2[6]) + np.array(choice[6])

for i in range(0, 7):
        result_2[i] = result_2[i].tolist()





st.title("📈 통계")



st.title("2학년(현 1학년)")

# 데이터 설정
ratio_1 = result_1[0]
labels_1 = ["정치와 법", "세계지리", "윤리와 사상", "세계사", "물리학1", "화학1", "생명과학1", "지구과학1"]

ratio_2 = result_1[1]
labels_2 = ["고전 읽기", "진로 영어", "확률과 통계", "프로그래밍"]

ratio_3 = result_1[2]
labels_3 = ["현대문학 감상", "영어권 문화", "기하", "빅데이터 분석"]

# Plotly로 파이 차트 생성
fig_1 = px.pie(values=ratio_1, names=labels_1, title="선택군1")
fig_2 = px.pie(values=ratio_2, names=labels_2, title="선택군2")
fig_3 = px.pie(values=ratio_3, names=labels_3, title="선택군3")

# Streamlit에 차트 표시
st.plotly_chart(fig_1)
st.plotly_chart(fig_2)
st.plotly_chart(fig_3)



st.title("3학년(현 2학년)")

# 데이터 설정
ratio_1 = result_2[0]
labels_1 = ["화법과 작문", "언어와 매체"]

ratio_2 = result_2[1]
labels_2 = ["미적분", "수학과제 탐구", "인공지능 수학"]

ratio_3 = result_2[2]
labels_3 = ["심화국어", "심화 영어 독해1", "심화 수학1"]

ratio_4 = result_2[3]
labels_4 = ["고전문학 감상", "심화 영어 독해2", "수학적 사고와 적분", "수학적 사고와 통계"]

ratio_5 = result_2[4]
labels_5 = ["생활과 윤리", "한국지리", "동아시아사", "사회·문화", "물리학2", "화학2", "생명과학2", "지구과학2"]

ratio_6 = result_2[5]
labels_6 = ["여행지리", "사회문제 탐구", "고전과 윤리", "생활과 과학", "융합과학", "자료구조"]

ratio_7 = result_2[6]
labels_7 = ["중국어", "일본어"]

# Plotly로 파이 차트 생성
fig_1 = px.pie(values=ratio_1, names=labels_1, title="선택군1")
fig_2 = px.pie(values=ratio_2, names=labels_2, title="선택군2")
fig_3 = px.pie(values=ratio_3, names=labels_3, title="선택군3")
fig_4 = px.pie(values=ratio_4, names=labels_4, title="선택군4")
fig_5 = px.pie(values=ratio_5, names=labels_5, title="선택군5")
fig_6 = px.pie(values=ratio_6, names=labels_6, title="선택군6")
fig_7 = px.pie(values=ratio_7, names=labels_7, title="선택군7")


# Streamlit에 차트 표시
st.plotly_chart(fig_1)
st.plotly_chart(fig_2)
st.plotly_chart(fig_3)
st.plotly_chart(fig_4)
st.plotly_chart(fig_5)
st.plotly_chart(fig_6)
st.plotly_chart(fig_7)