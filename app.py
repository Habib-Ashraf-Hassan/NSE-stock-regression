import streamlit as st
import joblib
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Load the trained model
model = joblib.load('ridge_model.pkl')

# Title of the app
st.title("Stock Day Price Predictor")

# Explanation of the app
st.write("Enter the values for the following features to predict the day price of the stock:")

# User input fields
low_12m = st.number_input("12m Low", min_value=0.0)
high_12m = st.number_input("12m High", min_value=0.0)
low_day = st.number_input("Day Low", min_value=0.0)
high_day = st.number_input("Day High", min_value=0.0)
previous = st.number_input("Previous", min_value=0.0)
volume = st.number_input("Volume", min_value=0.0)

# If the user submits the form
if st.button("Predict Day Price"):
    # Prepare the input data for prediction
    input_data = pd.DataFrame([[low_12m, high_12m, low_day, high_day, previous, volume]],
                              columns=['12m Low', '12m High', 'Day Low', 'Day High', 'Previous', 'Volume'])

    # Make prediction
    predicted_price = model.predict(input_data)

    # Calculate percentage change
    perc_change = (predicted_price - previous) / previous * 100

    # Display the result
    if predicted_price < previous:
        st.markdown(f"<h3 style='color:red;'>Predicted Day Price: {predicted_price[0]:.2f}</h3>", unsafe_allow_html=True)
    elif predicted_price > previous:
        st.markdown(f"<h3 style='color:green;'>Predicted Day Price: {predicted_price[0]:.2f}</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='color:orange;'>Predicted Day Price: {predicted_price[0]:.2f}</h3>", unsafe_allow_html=True)
        
    # # Optionally display the percentage change
    # st.write(f"Percentage Change from Previous: {perc_change}%")

