import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')  # Replace with your model file

# Custom CSS
st.markdown(
    """
    <style>
    /* Main title styling */
    h1 {
        color: #4CAF50;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 40px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }

    /* Header styling */
    h2 {
        color: #2196F3;
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        margin-bottom: 15px;
    }

    /* Input field styling */
    .stNumberInput, .stSelectbox, .stRadio {
        background-color: #f0f2f6;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 15px;
        border: 2px solid #ddd;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Focus effect on input fields */
    .stNumberInput:focus, .stSelectbox:focus, .stRadio:focus {
        border-color: #4CAF50;
        outline: none;
    }

    /* Button styling */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-size: 18px;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #45a049;
    }

    .stButton>button:active {
        background-color: #388e3c;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

    /* Success message styling */
    .stAlert {
        background-color: #d4edda;
        color: #155724;
        padding: 12px;
        border-radius: 8px;
        margin-top: 20px;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Additional section styling */
    .stMarkdown {
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Item Outlet Sales Prediction")

# Input fields for user data
st.header("Enter Item Details")

# Create input fields for each feature
item_identifier = st.selectbox("Item Identifier", ["FDA15", "DRC01", "FDN15", "FDX07", "NCD19"])
item_weight = st.number_input("Item Weight", min_value=0.0, value=9.30)
item_fat_content = st.selectbox("Item Fat Content", ["Low Fat", "Regular", "Non-Edible"])
item_visibility = st.number_input("Item Visibility", min_value=0.0, value=0.016047)
item_type = st.selectbox("Item Type", ["Dairy", "Soft Drinks", "Meat", "Fruits and Vegetables", "Household"])
item_mrp = st.number_input("Item MRP", min_value=0.0, value=249.8092)
outlet_identifier = st.selectbox("Outlet Identifier", ["OUT049", "OUT018", "OUT010", "OUT013"])
outlet_establishment_year = st.number_input("Outlet Establishment Year", min_value=1900, max_value=2023, value=1999)
outlet_size = st.selectbox("Outlet Size", ["Small", "Medium", "High"])
outlet_location_type = st.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"])
outlet_type = st.selectbox("Outlet Type", ["Supermarket Type1", "Supermarket Type2", "Grocery Store"])

# Create a dictionary from user input
input_data = {
    "Item_Identifier": item_identifier,
    "Item_Weight": item_weight,
    "Item_Fat_Content": item_fat_content,
    "Item_Visibility": item_visibility,
    "Item_Type": item_type,
    "Item_MRP": item_mrp,
    "Outlet_Identifier": outlet_identifier,
    "Outlet_Establishment_Year": outlet_establishment_year,
    "Outlet_Size": outlet_size,
    "Outlet_Location_Type": outlet_location_type,
    "Outlet_Type": outlet_type,
}

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Encode categorical variables (if needed)
# You can use the same encoding logic used during training
input_df = pd.get_dummies(input_df, columns=["Item_Fat_Content", "Item_Type", "Outlet_Identifier", "Outlet_Size", "Outlet_Location_Type", "Outlet_Type"])

# Ensure the input DataFrame has the same columns as the training data
# Add missing columns with default values
train_columns = model.feature_names_in_  # Replace with your training data columns
for col in train_columns:
    if col not in input_df.columns:
        input_df[col] = 0

# Reorder columns to match training data
input_df = input_df[train_columns]

# Predict button
if st.button("Predict Sales"):
    # Make prediction
    prediction = model.predict(input_df)
    st.success(f"Predicted Item Outlet Sales: {prediction[0]:.2f}")
