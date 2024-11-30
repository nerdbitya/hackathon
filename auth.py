import streamlit as st
from hashlib import sha256

USER_DB = {
  "bitya": sha256("12345678".encode()).hexdigest(),
  "alina": sha256("69420228".encode()).hexdigest(),
  "amir":  sha256("amir_lox".encode()).hexdigest(),
  "beks":  sha256("lox_amir".encode()).hexdigest(),
}

def authenticate(username, password):
  hashed_pw = sha256(password.encode()).hexdigest()
  return USER_DB.get(username) == hashed_pw

def do_auth():
  msg = {
    "msg": "",
    "msg_type": "",
  }
  if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

  if not st.session_state["authenticated"]:
    st.title("Вход")

    username = st.empty()
    password = st.empty()
    but = st.empty()
    username_ph = username.text_input("Имя пользователя")
    password_ph = password.text_input("Пароль", type="password")
    but_ph = but.button("Войти")
    if but_ph:
      if authenticate(username_ph, password_ph):
        st.session_state["authenticated"] = True
        st.success(f"Добро пожаловать, {username_ph}!")
        username.empty()
        password.empty()
        but.empty()
      else:
        st.error("Неправильное имя пользователя или пароль!")

  else:
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update(authenticated=False))