import streamlit as st

st.title("Тест")

# Въпрос 1
st.write("Коя е столицата на България?")
user_answer1 = st.text_input("Вашият отговор:", key="q1")
if st.button("Провери отговор 1"):
    if user_answer1.strip().lower() == "софия":
        st.success("Верен отговор!")
    else:
        st.error("Грешен отговор")

# Въпрос 2
st.write("Кога е създадена България?")
user_answer2 = st.text_input("Вашият отговор:", key="q2")
if st.button("Провери отговор 2"):
    if user_answer2.strip() == "681":
        st.success("Верен отговор!")
    else:
        st.error("Грешен отговор")

# Въпрос 3
st.write("Къде се намира Айфеловата кула?")
user_answer3 = st.text_input("Вашият отговор:", key="q3")
if st.button("Провери отговор 3"):
    if user_answer3.strip().lower() == "париж":
        st.success("Верен отговор!")
    else:
        st.error("Грешен отговор")

# Въпрос 4
st.write("Коя година е започнала Първата световна война?")
user_answer4 = st.text_input("Вашият отговор:", key="q4")
if st.button("Провери отговор 4"):
    if user_answer4.strip() == "1914":
        st.success("Верен отговор!")
    else:
        st.error("Грешен отговор")

