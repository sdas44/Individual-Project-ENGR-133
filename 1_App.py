import streamlit as st
from tasks import tasks   # adjust import if needed

st.set_page_config("Donna AI")

# ---- SESSION STATE INITIALIZATION ----
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "task" not in st.session_state:
    st.session_state.task = ""

if "details" not in st.session_state:
    st.session_state.details = ""

if "due_date" not in st.session_state:
    st.session_state.due_date = None


# ---- UI ----
st.title("Donna AI: The Automated Task Manager")
st.divider()

st.session_state.task = st.text_input("Enter your task:", key="task_input")
st.session_state.details = st.text_area("Task Details:", key="details_input")
st.session_state.due_date = st.date_input("Due Date:", key="due_date_input")

if st.button("Add Task"):
    new_task = tasks(
        title=st.session_state.task,
        details=st.session_state.details,
        due_date=st.session_state.due_date
    )

    st.session_state.tasks.append(new_task)

    # clear inputs
    st.session_state.task = ""
    st.session_state.details = ""
    st.session_state.due_date = None

st.divider()


# ---- DISPLAY TASKS ----
st.header("TO-DO List")

for i, t in enumerate(st.session_state.tasks):
    with st.expander(t.title):
        st.write("**Details:**", t.details)
        st.write("**Due:**", t.due_date)
        st.divider()

        # unique key per task
        if st.button("Mark as Completed", key=f"complete_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()
