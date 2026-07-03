# 🏡 End-to-End House Price Prediction Pipeline

## 📌 Project Overview
This project is an end-to-end Machine Learning application designed to predict real estate prices based on the California Housing Dataset. It demonstrates a complete data science workflow, from model training and saving (`joblib`) to serving the model via a high-performance **FastAPI** backend, and finally interacting with it through a user-friendly **Streamlit** frontend.

This repository serves as a practical implementation of building, validating, and consuming RESTful APIs for machine learning models.

## ✨ Key Features
* **Robust ML Engine:** Utilizes a pre-trained regression model to estimate house prices with high accuracy.
* **High-Performance API:** Built with **FastAPI**, offering asynchronous capabilities and significantly faster execution. 
* **Strict Data Validation:** Implements **Pydantic** schemas to ensure incoming payload validation and precise error handling (e.g., handling HTTP 422 errors).
* **Interactive Web Interface:** A sleek and intuitive frontend built with **Streamlit** that allows users to input housing metrics and instantly view price predictions.
* **Auto-Generated Documentation:** Interactive Swagger UI API documentation out-of-the-box.

## 🛠️ Technology Stack
* **Machine Learning:** `scikit-learn`, `numpy`, `joblib`
* **Backend Framework:** `FastAPI`, `uvicorn` (ASGI server)
* **Frontend Framework:** `Streamlit`, `requests`
* **Data Validation:** `Pydantic`

## 🏗️ Architecture & Workflow
1. **Client (Streamlit):** User inputs 8 specific housing features (e.g., Median Income, House Age, Population) via the web interface.
2. **HTTP POST Request:** The frontend packages the data into a JSON payload and sends it to the FastAPI endpoint (`/predict`).
3. **Backend Processing (FastAPI):** The API validates the JSON against the Pydantic schema. If valid, the data is converted into a 2D Numpy array.
4. **Prediction:** The pre-loaded `.joblib` model processes the array and calculates the estimated price.
5. **Response:** The API sends back a JSON response containing the predicted price, which Streamlit formats and displays to the user.


## ⚙️ How to Run This Project Locally

Follow these quick steps to get the application running on your machine.

**1. Clone the repository**
```bash
git clone [https://github.com/RafayTheAIEngineer/House-Price-Prediction-FastAPI.git](https://github.com/RafayTheAIEngineer/House-Price-Prediction-FastAPI.git)
cd House-Price-Prediction-FastAPI
```

**2. Install the required dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the FastAPI Backend**
Open a terminal and fire up the backend server:
```bash
uvicorn main:app --reload
```
(Note: Replace main with the name of your FastAPI Python file if it's different).

**4. Launch the Streamlit Frontend**
Open a second terminal window and run the dashboard:
```bash
streamlit run app.py
```
(Note: Replace app with the name of your Streamlit Python file if it's different).
