from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np 

# initialization 
app = FastAPI(title='House Price Prediction API')

# load save model 
model = joblib.load('Model_House_Price_Predictor.pkl')

# pydantic schema
class Housedata(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

    # Ye Config class sirf Postman/Swagger mein sample data dikhane ke liye hai
    class Config:
        json_schema_extra = {
            'example' : {
                'MedInc': 8.32,
                'HouseAge': 41.0,
                'AveRooms': 6.98,
                'AveBedrms': 1.02,
                'Population': 322.0,
                'AveOccup': 2.55,
                'Latitude': 37.88,
                'Longitude': -122.23
            }
        }


# post rout
@app.post('/predict')
def predict_price(data: Housedata):
    # Pydantic model se data nikal kar Numpy Array mein convert karna
    # Note: Model ko 2D array chahiye hota hai isliye do brackets [[ ]] use kiye hain
    features = np.array([[
        data.MedInc,
        data.HouseAge,
        data.AveRooms,
        data.AveBedrms,
        data.Population,
        data.AveOccup,
        data.Latitude,
        data.Longitude
    ]])

    # Model se prediction lena
    predicted_price = model.predict(features)

    # json format me result return kerna 
    return {
        'message' : 'Prediction successful',
        'predicted_price' : float(predicted_price[0])
    }