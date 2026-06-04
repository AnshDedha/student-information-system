import streamlit as st

st.title("Student Information System")
st.write("Enter student details and view the submitted information.")

student_name = st.text_input("Enter Student Name")

roll_number = st.number_input(
    "Enter Roll Number",
    min_value=1,
    step=1
)

course = st.selectbox(
    "Select Course",
    ["BCA", "B.Tech", "B.Sc", "B.Com", "MCA"]
)

subjects = st.multiselect(
    "Select Subjects",
    ["Python", "Java", "DBMS", "AWS", "MongoDB", "Machine Learning", "Data Science"]
)

marks = st.slider("Marks", 0, 100, 50)

if st.button("Submit"):
    if student_name.strip() == "":
        st.error("Student Name cannot be empty.")
    elif len(subjects) == 0:
        st.error("Please select at least one subject.")
    else:
        st.success("Student details submitted successfully!")

        st.subheader("Student Details")
        st.write("Student Name:", student_name)
        st.write("Roll Number:", roll_number)
        st.write("Course:", course)
        st.write("Subjects:", ", ".join(subjects))
        st.write("Marks:", marks)
