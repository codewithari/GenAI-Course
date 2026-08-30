import streamlit as st

st.title("🎓 Student Grade System")

student_name = st.text_input("Student Name")

mark = st.number_input(
    "Student Mark",
    min_value=0.0,
    max_value=100.0,
    value=None,
    step=1.0
)

if st.button("Calculate Grade"):

    if student_name.strip() == "":
        st.warning("Please enter the student name.")

    elif mark is None:
        st.warning("Please enter the student's mark.")

    else:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "E"

        st.success(
            f"Student {student_name} scored {mark:.0f} marks and received Grade {grade}."
        )