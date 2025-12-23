from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
import joblib
data = pd.read_csv("data\Housing.csv")

numeric_features = ["area", "bedrooms", "bathrooms", "stories", "parking"]

binary_features = [
    "mainroad", "guestroom", "basement",
    "hotwaterheating", "airconditioning", "prefarea"
]

categorical_features = ["furnishingstatus"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num",StandardScaler(),numeric_features),
        ("bin",OneHotEncoder(drop="if_binary"),binary_features),
        ("cat",OneHotEncoder(drop="first"),categorical_features)
    ]
)

model = Pipeline(
    steps=[
        ("preprocessing",preprocessor),
        ("regressor",LinearRegression())
    ]
)

X=data.drop("price",axis=1)
y=data["price"]

model.fit(X,y)
preds = model.predict(X)
print("R2 Score:",r2_score(y,preds))
joblib.dump(model,"model/house.joblib")
print("pipline saved")