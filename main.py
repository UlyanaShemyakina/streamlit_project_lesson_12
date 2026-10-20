import streamlit as st # streamlit run main.py 

# st.title("Калькулятор") # streamlit run main.py 
# # https://docs.streamlit.io/develop/api-reference/widgets/st.number_input
# val_1 = st.number_input("Insert a number", key="val_1")
# val_2 = st.number_input("Insert a number", key="val_2")
# st.write(f"Результат {val_1 + val_2}")


# сначала создаём pip freeze > reguerements.txt
# git add .
# git commit - "add req"
# git push

# чтобы опубликовать на гитхабе сначала
# git init
# создаём файлик .gitignore 
# git add .
# git commit -m "initial comit"
# создаём на github
# копирую отуда и вставляем в терминал git remote add origin https://github.com/UlyanaShemyakina/streamlit_project_lesson_12.git
# копирую отуда и вставляем в терминал git push -u origin main


# переменовала локальную ветку из мастер в mail env) git branch -M main 

# создаём переименовываем requirements
# Rename-Item reguerements.txt requirements.txt
# git add requirements.txt
# git commit -m "Add requirements.txt"


# удаляем reguerements.txt из репозитория
# git rm reguerements.txt - удаляет
# git commit -m "Remove misspelled requirements file" зафиксировать удаление в коммите
# git push отправляем на github



# text input 
# создать приложение, которое запрашивает у пользователя имя, фамилию и выводит в
# приветственном письме ниже

st.title("Добрый день") # streamlit run main.py 
# заходишь по ссылке, чтобы найти как писать питон
# https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
first_name = st.text_input("Set first name: ")
last_name = st.text_input("Set last name: ")

if first_name == "" and last_name == "":
    message = "Привет!"
else:
    message = f"Привет, {last_name} {first_name}!"

st.write(message)

# streamlit run main.py



if "show_text" not in st.session_state: # session_state - состояние
    st.session_state.show_text = False

config = {"show_text": False}

def show_handler():
    st.session_state.show_text = not st.session_state.show_text

st.button("**Кликни чтобы получить текст!**", on_click=show_handler)

if st.session_state.show_text:
    st.write("Спрятанное сообщение")

# чтобы за диплоить надо 
# git add .
# git commit -m "add new logic"
# git push