import pandas as pd
import joblib

model = joblib.load("model/house.joblib")

house_input = {
    "area": 7420,
    "bedrooms": 4,
    "bathrooms": 2,
    "stories": 3,
    "mainroad": "yes",
    "guestroom": "no",
    "basement": "no",
    "hotwaterheating": "no",
    "airconditioning": "yes",
    "parking": 2,
    "prefarea": "yes",
    "furnishingstatus": "furnished"
}

input_df = pd.DataFrame([house_input])

prediction=model.predict(input_df)
print("predicted price  :",prediction[0])