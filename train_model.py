from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib
import os

os.makedirs("models", exist_ok=True)

df = pd.read_csv("dataset/features.csv")
X = df[["protocol", "length"]]

model = IsolationForest(contamination=0.01)
model.fit(X)

joblib.dump(model, "models/isolation_forest.pkl")
print("✅ Model saved to models/isolation_forest.pkl")
