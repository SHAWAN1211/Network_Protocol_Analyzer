import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("results/detection_results.csv")

sns.countplot(data=df, x='protocol')
plt.title("Protocol Usage")
plt.show()

sns.scatterplot(data=df, x="length", y="protocol", hue="anomaly", palette={1:"green", -1:"red"})
plt.title("Anomalies")
plt.show()
