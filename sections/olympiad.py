import streamlit as st

from data import OLYMPIADS_DB

st.title("Олимпиады")

main_con = st.container()
sub_cons = list(tuple())

with main_con:
  for key, value in OLYMPIADS_DB.items():
    olympiad = st.container()
    left, mid, right = olympiad.columns(3)
    left.write(value[0])
    mid.write(str(value[1]))
    but = right.button("Зарегистрироваться", key=key)

    sub_cons.append(olympiad)