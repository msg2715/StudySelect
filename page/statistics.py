import streamlit as st
import plotly.express as px
import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()


# 2학년 선택과목 데이터 시각화
cursor.execute(f"SELECT choice FROM user WHERE usergrade=1")
row = cursor.fetchall()

for i in row:
    print(eval(i[0]))
    
# 데이터들을 합치는 코드 작성해야함,, :





st.title("📈 통계/분석")

# 데이터 설정
ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

# Plotly로 원형 차트 생성
fig = px.pie(values=ratio, names=labels, title="과일 비율")

# Streamlit에 차트 표시
st.plotly_chart(fig)