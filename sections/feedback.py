import streamlit as st

st.title("Обратная связь")

radio = st.radio(
  label="Анонимность",
  options=["Анонимно", "Под своим именем"]
)

if radio == "Под своим именем":
  name = st.text_input("Имя")

text = st.text_area("Вопрос, жалоба или предложение...")

button = st.button("PICKME")

if button:
  msg = {
    "name": "",
    "msg":  "",
  }
  if radio == "Под своим именем":
    msg["name"] = name
  else:
    msg["name"] = "Аноним"
  msg["msg"] = text

  print(msg)
  st.success("Сообщение отправлено!")