import streamlit as st
import matplotlib.pyplot as plt

st.title("통계/분석")

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

p = plt.pie(ratio, labels=labels, autopct='%.1f%%')

st.plotly_chart(p)