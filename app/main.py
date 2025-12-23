from fastapi import FastAPI
from app.schemas import HouseInput,HouseOutput
from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("model/random_house.joblib")

@app.get("/")
def health_check():
    return {"status":"api is running"}

@app.post("/predict",response_model=HouseOutput)
def predict_price(data:HouseInput):
    try:
        input_df=pd.DataFrame([data.dict()])
        prediction = model.predict(input_df)
        return {
            "result" : prediction 
        }
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
