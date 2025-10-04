import streamlit as st
import xgboost as xgb
import numpy as np

# Set the page configuration
st.set_page_config(page_title="Amazon+Delivery+Time+Prediction", layout="centered",page_icon="🚚")

# Title of the app
st.title("Amazon Delivery Time Prediction")

# Adding background image

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://static.vecteezy.com/system/resources/previews/000/455/506/large_2x/border-template-with-man-driving-folklift-vector.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
details={'age':1,'weather':'unknown', 'traffic':'unknown', 'vehicle':'unknown', 'area':'unknown','category':'unknown','distance':0 }
categorical_mapping = {'traffic': {'High ': 0, 'Jam ': 1, 'Low ': 2, 'Medium ': 3},
 'weather': {'Cloudy': 0,'Fog': 1, 'Sandstorms': 2,'Stormy': 3,'Sunny': 4,'Windy': 5},
 'vehicle': {'motorcycle ': 0, 'scooter ': 1, 'van': 2},
 'area': {'Metropolitian ': 0, 'Other': 1, 'Semi-Urban ': 2, 'Urban ': 3},
 'category': {'Apparel': 0, 'Books': 1, 'Clothing': 2, 'Cosmetics': 3, 'Electronics': 4,'Grocery': 5, 'Home': 6,'Jewelry': 7,
  'Kitchen': 8,'Outdoors': 9, 'Pet Supplies': 10, 'Shoes': 11, 'Skincare': 12, 'Snacks': 13, 'Sports': 14, 'Toys': 15}}

# Load the pre-trained model
model = xgb.XGBRegressor()
model.load_model('xgboost_model.json')

# Adding Select boxes for input features
st.header("Please provide the following details:")
col1, col2, col3, col4 = st.columns(4)

with col1:
    details['distance'] = st.number_input("Distance (in km)", min_value=1.0, step=0.1)
    details['weather'] = categorical_mapping['weather'][st.selectbox("Weather Condition", categorical_mapping['weather'].keys())]

with col2:
    details['traffic'] = categorical_mapping['traffic'][st.selectbox("Traffic Condition", categorical_mapping['traffic'].keys())]
    details['vehicle'] = categorical_mapping['vehicle'][st.selectbox("Vehicle Type", categorical_mapping['vehicle'].keys())]

with col3:
    details['area'] = categorical_mapping['area'][st.selectbox("Area Type", categorical_mapping['area'].keys())]
    details['category'] = categorical_mapping['category'][st.selectbox("Product Category", categorical_mapping['category'].keys())]

with col4:
    details['age'] = st.number_input("Dilevery agent's age", min_value=1, step=1)

def prediction(details):
    # Convert input details to a format suitable for prediction
    input_data = np.array(list(details.values())).reshape(1, -1)
    # Make prediction
    delivery_time = model.predict(input_data)
    return delivery_time[0]

# submit button
if st.button("Predict Delivery Time"):  
    #logic
    delivery_time = prediction(details)
    st.success(f"Estimated Delivery Time: {delivery_time:.2f} hours")
    st.balloons()