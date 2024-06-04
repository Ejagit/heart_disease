import streamlit as st
import pandas as pd
import numpy as np
import time
from xgboost import XGBClassifier
import pickle
import lightgbm
from lightgbm import LGBMRegressor
import os

# Check the current working directory
st.write("Current working directory:", os.getcwd())

# Load the trained model with caching
@st.cache_data
def load_model():
    return pickle.load(open('model/xgb_sm_model.pkl', 'rb'))

# Define the prediction function with caching
@st.cache_data
def predict(data):
    model = load_model()
    return model.predict(data)

# Streamlit app
st.title("Heart Disease Prediction App")

st.write("Enter the following information to predict the likelihood of heart disease:")

# Input fields
BMI = st.slider("BMI", 12.02, 94.85, 25.0)
Smoking = st.selectbox("Smoking", ["Yes", "No"])
AlcoholDrinking = st.selectbox("Alcohol Drinking", ["Yes", "No"])
Stroke = st.selectbox("Stroke", ["Yes", "No"])
PhysicalHealth = st.slider("Physical Health (last 30 days)", 0.0, 30.0, 10.0)
MentalHealth = st.slider("Mental Health (last 30 days)", 0.0, 30.0, 10.0)
DiffWalking = st.selectbox("Difficulty Walking", ["Yes", "No"])
Sex = st.selectbox("Sex", ["Male", "Female"])
AgeCategory = st.selectbox("Age Category", ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-older'])
Race = st.selectbox("Race", ['American Indian/Alaskan Native', 'Other', 'White', 'Black', 'Hispanic', 'Asian'])
Diabetic = st.selectbox("Diabetic", ['No', 'Yes', 'borderline diabetes', 'Yes (during pregnancy)'])
PhysicalActivity = st.selectbox("Physical Activity", ["Yes", "No"])
GenHealth = st.selectbox("General Health", ['Excellent', 'Good', 'Very good', 'Fair', 'Poor'])
SleepTime = st.slider("Sleep Time (hours)", 1.0, 24.0, 7.0)
Asthma = st.selectbox("Asthma", ["Yes", "No"])
KidneyDisease = st.selectbox("Kidney Disease", ["Yes", "No"])
SkinCancer = st.selectbox("Skin Cancer", ["Yes", "No"])

input_data = pd.DataFrame({
    'BMI': [BMI],
    'Smoking': [Smoking],
    'AlcoholDrinking': [AlcoholDrinking],
    'Stroke': [Stroke],
    'PhysicalHealth': [PhysicalHealth],
    'MentalHealth': [MentalHealth],
    'DiffWalking': [DiffWalking],
    'Sex': [Sex],
    'AgeCategory': [AgeCategory],
    'Race': [Race],
    'Diabetic': [Diabetic],
    'PhysicalActivity': [PhysicalActivity],
    'GenHealth': [GenHealth],
    'SleepTime': [SleepTime],
    'Asthma': [Asthma],
    'KidneyDisease': [KidneyDisease],
    'SkinCancer': [SkinCancer]
})

# Frequency encoding
freq_encode_cols = ['AgeCategory', 'Race', 'Diabetic']
for col in freq_encode_cols:
    freq = input_data[col].value_counts(normalize=True).to_dict()
    input_data[col] = input_data[col].map(freq)

# Ordinal encoding
ordinal_mapping = {'Excellent': 4, 'Very good': 3, 'Good': 2, 'Fair': 1, 'Poor': 0}
input_data['GenHealth'] = input_data['GenHealth'].map(ordinal_mapping)

# One-hot encoding
one_hot_cols = ['Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer']
input_data = pd.get_dummies(input_data, columns=one_hot_cols)

if st.button("Predict"):
    prediction = predict(input_data)
    if prediction[0] == 1:
        st.write("The model predicts that you are at risk of heart disease.")
    else:
        st.write("The model predicts that you are not at risk of heart disease.")




