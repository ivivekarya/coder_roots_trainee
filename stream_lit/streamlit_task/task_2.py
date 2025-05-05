"""2. Create a Streamlit multi-page application using streamlit-option-menu 
for navigation. The app should have multiple pages with different 
functionalities.
Requirements:
Home Page:
Displays a welcome message and an overview of the app.
Task Manager Page:
A form to add tasks with fields like task name, description, priority, and 
due date.
Displays a list of submitted tasks.
Functionality:
Users navigate between pages using an option menu in the sidebar."""

import streamlit as st
from streamlit_option_menu import option_menu
import datetime

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Task Manager"],
        icons=["house", "list-task"],
        menu_icon="cast",
        default_index=0,
    )

# Home Page
if selected == "Home":
    st.title("👋 Welcome to Task Tracker")

# Task Manager Page
elif selected == "Task Manager":
    st.title("🗂️ Task Manager")

    # Form to add task
    with st.form("task_form"):
        task_name = st.text_input("Task Name")
        description = st.text_area("Description")
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        due_date = st.date_input("Due Date", min_value=datetime.date.today())
        submitted = st.form_submit_button("Add Task")

    if submitted:
        st.success("✅ Task submitted successfully!")
        st.subheader("📋 Summary of Task:")
        st.write(f"**Task Name:** {task_name}")
        st.write(f"**Description:** {description}")
        st.write(f"**Priority:** {priority}")
        st.write(f"**Due Date:** {due_date}")

