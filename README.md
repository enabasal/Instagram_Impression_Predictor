📸Instagram_Impression_Predictor

This project is a Machine Learning web app that predicts the total impressions an Instagram post might receive, based on various post features like likes, shares, saves, hashtags, etc.
It was built using Streamlit for the frontend and Linear Regression for prediction.

🚀 How It Works
User inputs Instagram post features (e.g., likes, saves, comments).

The app scales the input data using a pre-fitted StandardScaler.

The scaled data is passed into a trained Linear Regression model.

The app predicts Total Impressions and categorizes the performance:
Poor, Average, Good, Very Good, or Excellent.

🛠️ Tech Stack
Python 3

Streamlit (for frontend)

Scikit-learn (for model building)

NumPy and Joblib (for data handling and model saving)

