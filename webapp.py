import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todoo= st.session_state["new_todo"]+ "\n"
    todos.append(todoo)
    functions.write_todos(todos)

st.title("My todo App")
st.subheader("Todo list")
st.write("This app is to improve our day to day activities")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" Enter todo to add ",
              placeholder="Add a todo",
              on_change=add_todo,key="new_todo")