import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student Academic Outcomes",
    page_icon="🎓"
)

st.title("🎓 Student Academic Outcomes Prediction")
st.write("Enter student information to predict Pass or Fail.")

# Load trained model
model = joblib.load("student_outcome_model.pkl")

attendance = st.slider("Attendance Percentage", 0, 100, 85)
study_hours = st.slider("Study Hours Per Day", 0.0, 12.0, 3.0)
previous_score = st.slider("Previous Exam Score", 0, 100, 70)
previous_gpa = st.slider("Previous GPA", 1.0, 4.0, 2.8)
assignment = st.slider("Assignment Completion Rate", 0, 100, 70)
time_management = st.slider("Time Management Score", 0, 100, 78)
sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0)

# Use original training categories
study_consistency = st.selectbox(
    "Study Consistency",
    sorted(["Low", "Medium", "High"])
)

revision_frequency = st.selectbox(
    "Revision Frequency",
    ["Rarely", "Daily", "Weekly"]
)

motivation_level = st.selectbox(
    "Motivation Level",
    sorted(["Low", "Medium", "High"])
)

input_data = pd.DataFrame([{
    "attendance_percentage": attendance,
    "study_hours_per_day": study_hours,
    "previous_exam_score": previous_score,
    "previous_gpa": previous_gpa,
    "assignment_completion_rate": assignment,
    "study_consistency": study_consistency,
    "revision_frequency": revision_frequency,
    "motivation_level": motivation_level,
    "time_management_score": time_management,
    "sleep_hours": sleep_hours
}])

if st.button("Predict Student Outcome"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Predicted Outcome: PASS 🎉")
    else:
        st.error("Predicted Outcome: FAIL ⚠️")
