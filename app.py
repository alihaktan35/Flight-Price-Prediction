
import streamlit as st
import pandas as pd
import joblib

# Load the trained model and preprocessor
model = joblib.load('flight_price_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

# Load the dataset to get unique values for dropdowns
df = pd.read_csv('dataset/Clean_Dataset.csv')
airline_list = df['airline'].unique()
source_city_list = df['source_city'].unique()
destination_city_list = df['destination_city'].unique()
departure_time_list = df['departure_time'].unique()
arrival_time_list = df['arrival_time'].unique()
stops_list = df['stops'].unique()
class_list = df['class'].unique()


# Initialize session state
if 'predicted_price' not in st.session_state:
    st.session_state.predicted_price = None

st.title('Flight Price Prediction')
st.markdown('[GitHub: alihaktan35](https://github.com/alihaktan35)')

# User inputs
airline = st.selectbox('Airline', airline_list)
source_city = st.selectbox('From City', source_city_list)
destination_city = st.selectbox('To City', destination_city_list)
departure_time = st.selectbox('Departure Time', departure_time_list)
arrival_time = st.selectbox('Arrival Time', arrival_time_list)
stops = st.selectbox('Stops', stops_list)
flight_class = st.selectbox('Class', class_list)
duration = st.number_input('Duration (hours)', min_value=0.1, max_value=50.0, value=2.0, step=0.1)
days_left = st.number_input('Days Left', min_value=1, max_value=50, value=1)


if st.button('Predict'):
    # Create a dataframe from user inputs
    input_data = pd.DataFrame({
        'airline': [airline],
        'source_city': [source_city],
        'destination_city': [destination_city],
        'departure_time': [departure_time],
        'arrival_time': [arrival_time],
        'stops': [stops],
        'class': [flight_class],
        'duration': [duration],
        'days_left': [days_left]
    })

    # Predict the price
    predicted_inr_price = model.predict(input_data)[0]
    st.session_state.predicted_price = predicted_inr_price * 0.47 # Convert to TRY

if st.session_state.predicted_price is not None:
    st.success(f'Predicted Flight Price: ₺ {st.session_state.predicted_price:,.2f}')
