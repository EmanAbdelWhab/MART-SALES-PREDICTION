# MART-SALES-PREDICTION
## Project Overview

The **Item Outlet Sales Prediction** project aims to predict the sales of items in various retail outlets based on a variety of features like item details, outlet characteristics, and market factors. The model is built using machine learning techniques to understand the relationships between input features and sales performance, enabling businesses to make more informed decisions regarding inventory management, promotions, and sales strategies.

## Importance of the Project

Predicting sales in retail settings is critical for efficient inventory management, maximizing profitability, and reducing waste. By predicting item sales accurately, businesses can:
- **Optimize Inventory Management**: Ensure that popular products are well-stocked and less popular ones do not take up valuable space.
- **Improve Pricing Strategies**: Set optimal prices for products based on their predicted sales performance.
- **Enhance Marketing Campaigns**: Identify which products are likely to perform well and tailor marketing efforts accordingly.
- **Increase Operational Efficiency**: Minimize overstocking and understocking issues, ensuring smooth supply chain operations.

This project leverages historical data on items and outlets, combined with machine learning models, to provide businesses with reliable sales predictions.

## Key Features
- Predicts **sales** for items based on a range of features including item type, weight, fat content, and outlet characteristics.
- Utilizes machine learning algorithms to build a robust predictive model.
- User-friendly interface for inputting new data and receiving predictions using **Streamlit**.

## How It Works

1. **Model Training**: A machine learning model is trained on a dataset that includes historical sales data, outlet information, and item attributes.
2. **Input Data**: The user inputs item and outlet details (such as item type, visibility, MRP, outlet size, etc.) into the web app.
3. **Prediction**: The trained model processes the input and predicts the sales for the item in the specified outlet.
4. **Result**: The prediction is displayed to the user as an estimated sales value.

## Video Demonstration

Watch this video to see how the app works and how to use it effectively:


https://github.com/user-attachments/assets/a3e0393e-98bc-4f47-a8a5-8337ee5ad991

## Technologies Used
- **Python**: Core language for implementing machine learning algorithms.
- **Streamlit**: A web framework to easily deploy the predictive model as a web app.
- **Pandas**: Data manipulation and preparation.
- **Joblib**: For saving and loading machine learning models.
- **Scikit-learn**: For building and training the predictive machine learning model.

## Installation

To get started with the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/item-outlet-sales-prediction.git
   ```

2. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser (usually accessible at `http://localhost:8501`).

## Usage

Once the app is running, you can input item details such as:
- Item identifier, weight, fat content, visibility, and MRP
- Outlet characteristics like size, type, location, and establishment year

Click on the **Predict Sales** button to get an estimated sales prediction for the entered data.
