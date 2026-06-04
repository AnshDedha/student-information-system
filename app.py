!pip install ipywidgets -q

import ipywidgets as widgets
from IPython.display import display, clear_output

title = widgets.HTML("<h2>Student Information System</h2>")
description = widgets.HTML("<p>Enter student details and view the submitted information.</p>")

name = widgets.Text(
    description='Name:',
    placeholder='Enter Student Name'
)

roll = widgets.IntText(
    description='Roll No:',
    value=1
)

course = widgets.Dropdown(
    options=['BCA', 'B.Tech', 'B.Sc', 'B.Com', 'MCA'],
    description='Course:'
)

subjects = widgets.SelectMultiple(
    options=['Python', 'Java', 'DBMS', 'AWS', 'MongoDB', 'Machine Learning', 'Data Science'],
    description='Subjects:'
)

marks = widgets.IntSlider(
    value=50,
    min=0,
    max=100,
    step=1,
    description='Marks:'
)

submit = widgets.Button(
    description='Submit',
    button_style='success'
)

output = widgets.Output()


def show_details(b):
    with output:
        clear_output()

        
        if name.value.strip() == "":
            print("❌ Error: Student Name cannot be empty.")
            return

        if len(subjects.value) == 0:
            print("❌ Error: Please select at least one subject.")
            return

        print("✅ Student details submitted successfully!\n")
        print("----- Student Details -----")
        print("Student Name :", name.value)
        print("Roll Number  :", roll.value)
        print("Course       :", course.value)
        print("Subjects     :", ", ".join(subjects.value))
        print("Marks        :", marks.value)

submit.on_click(show_details)

display(
    title,
    description,
    name,
    roll,
    course,
    subjects,
    marks,
    submit,
    output
)