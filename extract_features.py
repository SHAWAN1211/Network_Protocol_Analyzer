import pandas as pd

df = pd.read_csv("dataset/captured_data.csv")
df["protocol"] = df["protocol"].astype(int)
df["length"] = df["length"].astype(int)

df.to_csv("dataset/features.csv", index=False)
print("✅ Features saved to dataset/features.csv")
