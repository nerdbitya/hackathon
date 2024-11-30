import streamlit as st
import pandas as pd
import numpy as np

from auth import do_auth

do_auth()

pages = {
  "Навигация": [
    st.Page("sections/personal_account.py", title="Личный кабинет"),
    st.Page("sections/olympiad.py", title="Олимпиады"),
    st.Page("sections/surveys.py", title="Опросы"),
    st.Page("sections/feedback.py", title="Обратная связь"),
  ]
}

if st.session_state["authenticated"]:
  pg = st.navigation(pages)
  pg.run()

else:
  pg = st.Page("sections/login.py", title="Вход")
