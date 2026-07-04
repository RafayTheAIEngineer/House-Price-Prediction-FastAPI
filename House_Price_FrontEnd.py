import streamlit as st 
import requests 

st.set_page_config(page_title="AI-House-Estimator", page_icon="🏢", layout="wide")

# sidebar setup
st.sidebar.title('🏠House Price Prediction App')
st.sidebar.write('Enter Your House Features and find out the price')

# styling and title of UI
st.title('🏠House Price Prediction')
st.write("Enter your california home's features and find out the price.")

st.markdown('---')

# create a form for taking user input 
st.header('Home Features')
col_1, col_2 = st.columns(2)

with col_1:
    med_inc = st.number_input('Median Income (MedInc)', value=8.32)
    ave_rooms = st.number_input('Average Rooms', value=6.98)
    population = st.number_input('Population', value=322.0)
    latitude = st.number_input('Latitude', value=37.88)

with col_2:
    house_age = st.number_input('House Age', value=41.0)
    ave_bedrms = st.number_input('Average Bedrooms', value=1.02)
    ave_occupy = st.number_input('Average Occupancy', value=2.55)
    longitude = st.number_input('Longitude', value=122.23)

st.markdown('---')

# predict button and fastapi call 
if st.button('Predict Price🚀'):
    data = {
        'MedInc': med_inc,
        'HouseAge': house_age,
        'AveRooms': ave_rooms,
        'AveBedrms': ave_bedrms,
        'Population': population,
        'AveOccup': ave_occupy,
        'Latitude': latitude,
        'Longitude': longitude
    }

    try:
        response = requests.post('https://house-price-prediction-fastapi-ndmd.onrender.com/predict', json=data)
        
        if response.status_code == 200 :
            result = response.json()
            raw_price = result['predicted_price']

            # The model's price is generally quoted in terms of '100k' (e.g., 3.52 = $352,000)
            formatted_price = raw_price * 100000

            st.success(f"**Predicted House Price : ${formatted_price:,.2f}**")

        else :
            # Yeh line humein FastAPI ka exact error dikhayegi
            st.error(f"API Error Code {response.status_code}: {response.text}")

            st.error('Did not receive a valid response from the API. Check the data.')

    except Exception as e:
        st.error(f'Could not connect to the API. Make sure FastAPI is running! Error: {e}')
