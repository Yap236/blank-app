import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Load trained model
rf = load("Random_Forest.joblib")

st.title("🎓 Student Placement Prediction App")
st.write("Enter student details below:")

# Input fields
IQ = st.number_input("IQ (0-200)", min_value=0, max_value=200, step=1)
CGPA = st.number_input("CGPA (0-10)", min_value=0.0, max_value=10.0, step=0.1)
Communication_Skills = st.number_input("Communication Skills (0-10)", min_value=0, max_value=10, step=1)
Projects_Completed = st.number_input("Projects Completed (0-5)", min_value=0, max_value=5, step=1)

# Prediction button
if st.button("Predict Placement"):
    user_input = [IQ, CGPA, Communication_Skills, Projects_Completed]
    
    input_array = np.array(user_input).reshape(1, -1)
    predicted_value = rf.predict(input_array)[0]
    
    result = "✅ Placed" if predicted_value == 1 else "❌ Not Placed"
    st.subheader(f"Prediction: {result}")