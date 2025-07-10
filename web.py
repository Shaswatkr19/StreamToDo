import streamlit as st
import functions


st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
                    rgba(0,0,0,0.6),
                    rgba(0,0,0,0.6)
                  ),
                  url("https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=1600&q=80");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    /* Input box style */
    input {
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        border: 1px solid #555;
        border-radius: 5px;
        padding: 10px;
    }

    /* Checkbox text color fix */
    div.row-widget.stCheckbox > label {
        color: white !important;
    }

    /* Title and subtitle styling */
    .stTitle, .stMarkdown h1, .stMarkdown h2 {
        color: white !important;
    }

    /* Warning style */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid #aaa;
        color: white;
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
