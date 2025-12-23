
# 🏠 House Price Prediction API

An **end-to-end Machine Learning project** that predicts house prices using a trained regression model, deployed as a **FastAPI service** with proper validation, testing, and CI workflow.

This project demonstrates **real-world ML engineering**, not just model training.

---

## 🚀 Project Highlights

- End-to-end ML pipeline (preprocessing + model)
- Uses **all features together** via `sklearn Pipeline`
- Deployed as a **FastAPI REST API**
- **Pydantic validation** for safe inputs
- **pytest** for automated testing
- **GitHub Actions CI** for reliability
- Production-ready structure

---

## 🧠 Problem Statement

Given house-related features such as area, number of rooms, amenities, and furnishing status, predict the **house price** accurately.

---

## 📊 Features Used

| Feature | Description |
|------|------------|
| area | Total house area (sqft) |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| stories | Number of floors |
| parking | Parking spaces |
| mainroad | Connected to main road (yes/no) |
| guestroom | Guest room available |
| basement | Basement availability |
| hotwaterheating | Hot water heating |
| airconditioning | AC availability |
| prefarea | Preferred area |
| furnishingstatus | Furnishing level |

🎯 **Target:** `price`

---

## 🧩 ML Approach

- **Numerical features** → StandardScaler  
- **Binary categorical features** → One-hot encoding  
- **Multi-class categorical features** → One-hot encoding  
- **Model** → Linear Regression  or Random Forest Regressor

All steps are combined using a **single sklearn Pipeline** to ensure:
- No data leakage
- Consistent preprocessing during inference

---

## 🏗️ Project Structure

```

housepricing/
├── app/
│   ├── main.py        # FastAPI app
│   └── schemas.py    # Pydantic models
│
├── model/
│   └── house_price_pipeline.joblib
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
└── README.md

````

---

## 🔮 API Usage

### ▶️ Run the API
```bash
uvicorn app.main:app --reload
````

Open:

```
http://127.0.0.1:8000/docs
```

---

### 📥 Sample Request

```json
{
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
```

---

### 📤 Sample Response

```json
{
  "predicted_price": 13284567.23
}
```

---

## 🧪 Testing

All endpoints are covered with automated tests.

```bash
pytest
```

Tests are executed:

* Locally
* Automatically on every push via **GitHub Actions**

---

## 🔄 CI/CD Workflow

* GitHub Actions runs:

  * Dependency installation
  * pytest execution
* Ensures code quality & reproducibility

✔️ No “works on my machine” issues

---

## 🎯 Why This Project Matters

This project demonstrates:

* ML + Backend integration
* Production-grade API design
* Clean preprocessing & inference
* Testing & CI discipline

> This is how **real ML systems** are built and shipped.

---

## 🧑‍💻 Author

**Rupesh Singh**
B.Sc. Computer Science
Aspiring ML / AI Engineer

---

## 📌 Future Improvements

* Replace Linear Regression with RandomForest / XGBoost
* Add batch prediction endpoint
* Deploy to cloud (Render / Fly.io)
* Add monitoring & logging

---

⭐ If you find this project useful, give it a star!





