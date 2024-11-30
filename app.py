import streamlit as st
import pandas as pd
import numpy as np

from auth import do_auth

do_auth()

pages = {
  "Навигация": [
    st.Page("pages/personal_account.py", title="Личный кабинет"),
    st.Page("pages/olympiad.py", title="Олимпиады"),
    st.Page("pages/surveys.py", title="Опросы"),
    st.Page("pages/feedback.py", title="Обратная связь"),
  ]
}

if st.session_state["authenticated"]:
  pg = st.navigation(pages)
  pg.run()

else:
  pg = st.Page("pages/login.py", title="Вход")
