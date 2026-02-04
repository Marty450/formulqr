import streamlit as st

st.title("📋 Мини тест – География")

st.write("### Въпрос:")
st.write("Коя е столицата на България?")

user_answer = st.text_input("Вашият отговор:")

if st.button("Провери отговора"):
    correct_answer = "София"

    if user_answer.strip().lower() == correct_answer.lower():
        st.success("✅ Верен отговор! Браво!")
    else:
        st.error("❌ Грешен отговор. Верният е: София")
