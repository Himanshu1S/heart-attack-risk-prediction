import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.title("Heart Attack Prediction")
st.markdown("Provide the following details")

age = st.slider("age , 18,100,40")
sex = st.selectbox("SEX" , ["M" , "F"])
chest_pain = st.selectbox("chest pain type" , ["ATA" , "NAP" , "TA" , "ASY"])
resting_bp = st.number_input("resting blood pressure(mm Hg)" , 80 , 200 , 120)
cholesterol = st.number_input("cholesterol (mg/dl)" , 100 , 600 , 200)
fasting_bs = st.selectbox("fasting blood sugar > 120 mg/dl" , [0,1])
resting_ecg = st.selectbox("resting ecg" , ["normal" , "ST" , "LVH"])
max_hr = st.slider("max heart rate" , 60,220,150)
exercise_angina = st.selectbox("exercise-induced angina" , ["Y" , "N"])
oldpeak = st.slider("oldpeak(ST depression)" , 0.0 , 0.6 , 1.0)
st_slope = st.selectbox("ST Slope" , ["up" , "flat" , "down"])


# Execute the code when the user clicks the Predict button
if st.button("predict"):
    # Store the user's health information in a dictionary
    raw_input = {
        # Numerical features: store the values directly
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        # Categorical features: convert selections into one-hot encoded features
        # 1 indicates the selected category like sex + m = 1 i.e sex_m = 1
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

# Convert the raw_input dictionary into a Pandas DataFrame.
# Each dictionary key becomes a column, and its value becomes a row entry.
# [raw_input] creates a single-row DataFrame for the user's input.
    input_df = pd.DataFrame([raw_input])

    # Loop through all columns expected by the trained model.
    for col in expected_columns:
    # Check if a required column is missing from the input DataFrame.
        if col not in input_df.columns:
    # Add the missing column and assign 0 because the category was not selected.
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]


    if prediction == 1:
        st.error("High Risk Of Heart Attack")
    else:
        st.success("Low Ris Of Heart Attack")