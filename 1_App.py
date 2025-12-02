import streamlit as st
from tasks import tasks   # adjust import if needed
from azure_transcribe import transcribe_continuous_with_timeout
from actionize_text import actionize_text, text_to_actions_file
import json
from mutagen.mp3 import MP3

st.set_page_config("Donna")

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
st.title("Donna: The Automated Task Manager")
st.divider()

st.session_state.task = st.text_input("Enter your task:", key="task_input")
st.session_state.details = st.text_area("Task Details:", key="details_input")
st.session_state.due_date = st.date_input("Due Date:", key="due_date_input")

if st.button("Add Task"):
    if st.session_state.task.strip() == "": # error handling for empty task titles
        st.warning("Please enter a task title.")
    else:
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

audio_task = st.audio_input("Explain Your Tasks VIA Audio", key="audio_input")

if st.button("Process Audio Task") and audio_task is not None:
    # Save file to your machine
    with open("user_audio_task.wav", "wb") as f:
        f.write(audio_task.getvalue())

    st.success("Audio saved as user_audio.wav")
    audio_info = MP3("user_audio_task.wav")
    if audio_info.info.length < 10: # error handling for short and excessively long audio inputs
        st.warning("Please provide a longer audio input (at least 10 seconds).")
    elif audio_info.info.length > 1000000:
        st.warning("Audio Input Too Long. Please limit to under ~3 hours.")
    else:
        text_transcript = transcribe_continuous_with_timeout("user_audio_task.wav", timeout_seconds=20)
        action_text = actionize_text(text_transcript)
        text_to_actions_file(action_text, output_path="audio_extracted_tasks.json")
        # go through the json file created and add all the tasks to seesion state
        with open("audio_extracted_tasks.json", "r") as f:
            action_json = json.load(f)
            for task in action_json["tasks"]:
                new_task = tasks(
                    title=task["name"],
                    details=task["description"],
                    due_date=task["due_date"]
                )
                st.session_state.tasks.append(new_task)
        
        audio_task = None

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
