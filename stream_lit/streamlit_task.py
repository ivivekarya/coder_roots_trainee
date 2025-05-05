"""1. Create a Streamlit-based form where users can submit task details.
 The form should include the following elements:

Task Name: A text input field to enter the task name.
Task Description: A text area for detailed task information.
Priority Selection: A radio button to select the priority level
 (Low, Medium, High).
Due Date: A date picker to select the deadline.
Completion Status: A checkbox to mark if the task is completed.
Submit Button: On submission, the entered details should be 
displayed as a summary.

Expected Functionality:

Users fill out the form and click submit.
A success message appears upon submission.
The task details are displayed dynamically below the form.
"""

import streamlit as st


st.header("TASKA")
st.subheader("Your task manager")

a=st.text_input("Task Name", placeholder='Enter Task Name here...')

b=st.text_area("Description")
priority=("Low","Medium","High")
pror = st.radio("select the priority level",priority)
e=st.date_input("due date")

st.checkbox("task completed")


# btn= st.button("Save")
if  st.button("submit"):
    st.success("Task submitted successfully!")
    # Display summary
    st.subheader("Summary of task :")
    st.write(f"**task Name:** {a}")
    st.write(f"**Description:** {b}")
    st.write(f"**priority:** {pror}")
    st.write(f"**due date:** {e}")

