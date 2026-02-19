# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy dataset (you can replace with real data later)
data = {
    "crime_rate": [10, 80, 40, 90, 20, 60, 30, 70],
    "lighting":   [1, 0, 1, 0, 1, 0, 1, 0],  # 1 = good lighting, 0 = poor
    "crowd":      [1, 0, 1, 0, 1, 0, 1, 0],  # 1 = crowded, 0 = isolated
    "risk":       [0, 2, 1, 2, 0, 2, 1, 2]   # 0=Low, 1=Medium, 2=High
}

df = pd.DataFrame(data)
X = df[["crime_rate", "lighting", "crowd"]]
y = df["risk"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "risk_model.pkl")
print("Model trained & saved as risk_model.pkl")