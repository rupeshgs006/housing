import joblib
import pandas as pd

# Load trained pipeline
pipeline = joblib.load("model/random_house.joblib")

preprocessor = pipeline.named_steps["preprocessing"]
model = pipeline.named_steps["regressor"]

# Get feature names after preprocessing
num_features = preprocessor.named_transformers_["num"].get_feature_names_out()
bin_features = preprocessor.named_transformers_["bin"].get_feature_names_out()
cat_features = preprocessor.named_transformers_["cat"].get_feature_names_out()

all_features = list(num_features) + list(bin_features) + list(cat_features)

# Get importance
importances = model.feature_importances_

importance_df = pd.DataFrame({
    "feature": all_features,
    "importance": importances
}).sort_values(by="importance", ascending=False)

print(importance_df.head(10))
