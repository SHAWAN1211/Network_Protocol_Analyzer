import pandas as pd
import joblib
import os

os.makedirs("results", exist_ok=True)

model = joblib.load("models/isolation_forest.pkl")
df = pd.read_csv("dataset/features.csv")

X = df[["protocol", "length"]]
predictions = model.predict(X)

df["anomaly"] = predictions
df.to_csv("results/detection_results.csv", index=False)

print("✅ Anomalies saved to results/detection_results.csv")
print("\n🔍 Anomalies Detected:")
print(df[df["anomaly"] == -1])
