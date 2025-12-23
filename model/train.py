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

model1 = Pipeline(
    steps=[
        ("preprocessing",preprocessor),
        ("regressor",LinearRegression())
    ]
)

model2 = Pipeline(
    steps=[
        ("preprocessing",preprocessor),
        ("regressor",RandomForestRegressor(
            n_estimators=300,
            random_state=42,
            n_jobs=1
        ))
    ]
)

X=data.drop("price",axis=1)
y=data["price"]

model1.fit(X,y)
model2.fit(X,y)
preds1 = model1.predict(X)
preds2 = model2.predict(X)
print("R2 Score:",r2_score(y,preds1))
print("R2 Score:",r2_score(y,preds2))
joblib.dump(model1,"model/house.joblib")
joblib.dump(model1,"mode2/random_house.joblib")
print("pipline saved")
