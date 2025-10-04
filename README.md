# 🚚 Amazon Delivery Time Prediction

This project predicts delivery time for Amazon orders based on real-world factors like distance, traffic, weather, and product category. It uses a regression model trained on historical delivery data and is deployed via Streamlit for interactive use.

---

## 📦 Features

- Predicts delivery time using:
  - Distance (km)
  - Weather and traffic conditions
  - Vehicle and area type
  - Product category
  - Delivery agent's age
- Interactive Streamlit UI
- MLflow integration for experiment tracking and model management
- Dataset profiling and metadata logging

---

## 🧠 Model Overview

- **Algorithm**: Linear Regression
- **Framework**: scikit-learn
- **Tracking**: MLflow
- **Deployment**: Streamlit

---

## 📊 Dataset Description

- **Source**: Synthetic or anonymized delivery logs
- **Features**:
  - `Distance`: Delivery distance in kilometers
  - `Weather Condition`: Sunny, Rainy, etc.
  - `Traffic Condition`: Low, Medium, High
  - `Vehicle Type`: Bike, Car, etc.
  - `Area Type`: Urban, Suburban, Metropolitan
  - `Product Category`: Grocery, Electronics, etc.
  - `Agent Age`: Age of delivery personnel
- **Target**: Delivery time in hours

Dataset metadata is logged using MLflow’s `PandasDataset` wrapper for reproducibility and schema tracking.

---

## 🧪 MLflow Integration

MLflow is used to:

- Track model parameters, metrics, and artifacts
- Log dataset metadata and input examples
- Register and version models for deployment

---
## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/DURRAINk/Amazon_Dilevery_Time_Prediction.git
cd Amazon_Dilevery_Time_Prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Launch the Streamlit App
```bash
streamlit run app.py
```
### 4. Start MLflow Tracking UI (Optional)
In `eda.ipynb`, there is the code for MLflow
1. launch the UI:
```bash
   mlflow ui
```
2. copy and paste your localhost uri in the notebook:
```python
# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri="http://127.0.0.1:5000/")
```
3. Run the code


