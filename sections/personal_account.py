import streamlit as st
from data import BALANCE_DB

st.title("Личный кабинет")

info = st.container(border=True)

columns = st.columns(4)
columns[0].image("resources/avatar.jpeg", None, 100)
columns[1].write("bitya :sunglasses:")
columns[1].write(f"Баллы: {BALANCE_DB.get("bitya")}")

with st.expander("Как получить баллы?"):
  st.write('''
           Активно учавствуйте на уроках и олимпиадах, создавайте проекты и ваш
           баланс будет автоматически пополнятся.
           ''')

with st.expander("Для чего нужны баллы?"):
  st.write('''
           Баллы можно обменять на бесплатные уроки и призы.
           ''')