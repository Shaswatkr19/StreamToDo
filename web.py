import streamlit as st
import functions


st.markdown(
    """
    <style>
    /* ---------- FULL-WIDTH BACKGROUND IMAGE ---------- */
    .stApp {
        /* black overlay, 60 % opacity */
        background: linear-gradient(
                    rgba(0,0,0,0.6),     /* top – black @60 % */
                    rgba(0,0,0,0.6)      /* bottom – black @60 % */
                  ),
                  url("https://images.pexels.com/photos/3201468/pexels-photo-3201468.jpeg");

        background-size: cover;          /* always fill screen */
        background-position: center;     /* keep subject centred */
        background-repeat: no-repeat;
        background-attachment: fixed;    /* parallax-style stay-put */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    .st-emotion-cache-1dp5vir {visibility: hidden;}
    .st-emotion-cache-6qob1r {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)

st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(
    label="New Todo", placeholder="Add new todo...",
                  label_visibility="collapsed", on_change=add_todo, key="new_todo")

st.warning("⚠️ Note: This is a shared demo. All users see and edit the same todo list.")
