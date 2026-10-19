import streamlit as st

st.title("Калькулятор") # streamlit run main.py 
# https://docs.streamlit.io/develop/api-reference/widgets/st.number_input
val_1 = st.number_input("Insert a number", key="val_1")
val_2 = st.number_input("Insert a number", key="val_2")
st.write(f"Результат {val_1 + val_2}")

# сначала создаём pip freeze > reguerements.txt
# чтобы опубликовать на гитхабе сначала
# git init
# создаём файлик .gitignore 
# git add .
# git commit -m "initial comit"
# создаём на github
# копирую отуда и вставляем в терминал git remote add origin https://github.com/UlyanaShemyakina/streamlit_project_lesson_12.git
# копирую отуда и вставляем в терминал git push -u origin main