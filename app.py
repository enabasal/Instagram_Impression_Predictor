import streamlit as st
import numpy as np
import joblib

# Load the saved model and scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title('📈 Instagram Post Impressions Predictor')
st.write('Fill in the post details below to predict total impressions.Please enter only numeric values in the input fields.')
st.write('The model predicts the number of impressions based on various features of your Instagram post.')

# Function to take number input properly
def get_int_input(label):
    value = st.text_input(label)
    try:
        return float(value.replace(",","").strip())
    except:
         st.warning(f"Please enter a valid number for {label}.")
        st.stop()

# User Inputs
from_home = get_int_input('From Home (Reach from Home Page)')
from_hashtags = get_int_input('From Hashtags (Reach via Hashtags)')
from_explore = get_int_input('From Explore (Reach via Explore Page)')
from_other = get_int_input('From Other (Other Sources Reach)')
saves = get_int_input('Number of Saves')
comments = get_int_input('Number of Comments')
shares = get_int_input('Number of Shares')
likes = get_int_input('Number of Likes')
profile_visits = get_int_input('Profile Visits')
follows = get_int_input('Follows')
caption_length = get_int_input('Caption Length (in characters)')
hashtags_count = get_int_input('Hashtags Count')
has_popular_hashtag = st.selectbox('Has Popular Hashtag?', ['Yes', 'No'])

# Convert 'Yes'/'No' to 1/0
has_popular_hashtag_value = 1 if has_popular_hashtag == 'Yes' else 0

# Create a button to make prediction
if st.button('🚀 Predict Impressions'):
    input_data = np.array([[from_home, from_hashtags, from_explore, from_other,
                            saves, comments, shares, likes, profile_visits,
                            follows, caption_length, hashtags_count, has_popular_hashtag_value]])

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Make the prediction
    prediction = model.predict(input_data_scaled)
    predicted_impressions = int(prediction[0])

    st.success(f"🎯 Predicted Impressions: {predicted_impressions}")

    # Categorize performance based on predicted impressions
    if predicted_impressions <= 500:
        performance = 'Poor'
        color = '#ff4d4d'  # Red
    elif predicted_impressions <= 1500:
        performance = 'Average'
        color = '#ffa64d'  # Orange
    elif predicted_impressions <= 5000:
        performance = 'Good'
        color = '#4da6ff'  # Blue
    elif predicted_impressions <= 10000:
        performance = 'Very Good'
        color = '#85e085'  # Light green
    else:
        performance = 'Excellent'
        color = '#33cc33'  # Dark green

    # Display the performance nicely
    st.markdown(f"<h2 style='color:{color}; text-align:center;'>{performance}</h2>", unsafe_allow_html=True)
