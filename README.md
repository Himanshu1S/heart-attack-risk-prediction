# 🫀 Heart Attack Risk Prediction

A Machine Learning project that uses a trained K-Nearest Neighbors (KNN) model to estimate the likelihood of heart disease based on user-provided health information.

## 📌 Project Overview

This project demonstrates how Machine Learning can be used to classify health-related data. A Streamlit application allows users to enter health information and receive a model prediction.

**Important:** This is an educational project, not a medical diagnostic tool. Its predictions should not be used to diagnose heart disease or make medical decisions.

## ✨ Features

* Interactive Streamlit interface
* K-Nearest Neighbors (KNN) classification model
* Input scaling using a saved scaler
* Consistent feature ordering using saved column information
* Prediction based on user-provided health information

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

## 📁 Project Structure

```text
mlproj1/
├── app.py
├── KNN_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate into the project directory

```bash
cd mlproj1
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only. It does not replace professional medical advice, diagnosis, or treatment.

## 👨‍💻 Author

**Himanshu Singh**

B.Tech CSE (AIML) Student
