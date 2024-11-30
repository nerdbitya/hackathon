import streamlit as st

st.title("Опросы")

st.write("Почему Вы решили заниматься робототехникой?")
texts = {
  1: st.empty(),
  2: st.empty(),
  3: st.empty(),
}

st.write("Что Вам больше всего нравится в программировании (программирование, \
          сборка роботов, искуственный интеллект и т.д.)?")
texts.append(st.text_area("Ответ", key=2))

st.write("Есть ли у Вас проект или идея, которую Вы хотели бы реализовать?")
texts.append(st.text_area("Ответ", key=3))

but = st.button("Отправить")
if but:
  msg = {
    "answer1": texts[0],
    "answer2": texts[1],
    "answer3": texts[2],
  }
  print(msg)
  for text in texts:
    text = st.empty()