import streamlit as st
from joblib import load
import numpy as np

# Load the trained model
model = load('Random_Forest.joblib')

st.title("Student Placement Prediction App 🎓")

st.write("Enter student details to predict placement outcome:")

# Input fields for all 8 features
IQ = st.number_input('IQ', min_value=-5.0, max_value=5.0, step=0.01, format="%.2f")
Prev_Sem_Result = st.number_input('Previous Semester Result', min_value=-5.0, max_value=5.0, step=0.01, format="%.2f")
CGPA = st.number_input('CGPA', min_value=-5.0, max_value=5.0, step=0.01, format="%.2f")
Academic_Performance = st.number_input('Academic Performance', min_value=-5.0, max_value=5.0, step=0.01, format="%.2f")
Internship_Experience = st.selectbox('Internship Experience', [0, 1])  # 0 = No, 1 = Yes
Extra_Curricular_Score = st.number_input('Extra Curricular Score', min_value=-5.0, max_value=5.0, step=0.01, format="%.2f")
Communication_Skills = st.number_input('Communication Skills', min_value=-5.0, max_value=5.0, step=0.01, format="%.2f")
Projects_Completed = st.number_input('Projects Completed', min_value=-5.0, max_value=5.0, step=0.01, format="%.2f")

# Prepare input array
input_array = np.array([[IQ, Prev_Sem_Result, CGPA, Academic_Performance,
                         Internship_Experience, Extra_Curricular_Score,
                         Communication_Skills, Projects_Completed]])

# Prediction button
if st.button('Predict Placement'):
    prediction = model.predict(input_array)
    result = "Placed" if prediction[0] == 1 else "Not Placed"
    st.subheader(f"Prediction: {result}")
