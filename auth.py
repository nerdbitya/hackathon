import streamlit as st
from hashlib import sha256
from data import USER_DB

def authenticate(username, password):
  hashed_pw = sha256(password.encode()).hexdigest()
  return USER_DB.get(username) == hashed_pw

def do_auth():
  if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

  if not st.session_state["authenticated"]:
    title = st.empty()
    title.title("Вход")

    username = st.empty()
    password = st.empty()
    but = st.empty()
    username_ph = username.text_input("Имя пользователя")
    password_ph = password.text_input("Пароль", type="password")
    if but.button("Войти"):
      if authenticate(username_ph, password_ph):
        st.session_state["authenticated"] = True
        st.success(f"Добро пожаловать, {username_ph}!")
        username.empty()
        password.empty()
        but.empty()
        title.empty()
      else:
        st.error("Неправильное имя пользователя или пароль!")

  else:
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update(authenticated=False))