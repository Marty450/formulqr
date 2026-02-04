import streamlit as st
st.title("Тест")
st.write("Коя е столицата на България?")
user_answer1 = st.text_input("Вашият отговор:")
if st.button("Провери отговора"):
    correct_answer1 = "София"
    if user_answer.strip().lower() == correct_answer1.lower():
        st.success("Верен отговор!")
    else:
        st.error("Грешен отговор")

st.write("Кога е създадена България?")
user_answer2 = st.text_input("Вашият отговор:")
if st.button("Провери отговора"):
    correct_answer2 = "681"
    if user_answer2.strip().lower() == correct_answer2.lower():
        st.success("Верен отговор!")
    else:
        st.error("Грешен отговор")

st.write("Къде се намира айфеловата кула")
user_answer3 = st.text_input("Вашият отговор:")
if st.button("Провери отговора"):
    correct_answer3 = "Париж"
    if user_answer3.strip().lower() == correct_answer3.lower():
        st.success("Верен отговор!")
    else:
        st.error("Грешен отговор")

st.write("Коя година е започнал 1 световна война")
user_answer4 = st.text_input("Вашият отговор:")
if st.button("Провери отговора"):
    correct_answer4 = "София"
    if user_answer4.strip().lower() == correct_answer4.lower():
        st.success("Верен отговор!")
    else:
        st.error("Грешен отговор")
