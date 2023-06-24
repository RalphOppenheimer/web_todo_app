import streamlit as st
import functions as fn

todos = fn.get_todos()

st.set_page_config(layout='wide')


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    print(new_todo)
    todos.append(new_todo)
    fn.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your <b>productivity</b>", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox)
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Entry", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

# For debug only
# st.session_state