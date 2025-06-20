import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌐 Network Analyzer Dashboard")

df = pd.read_csv("results/detection_results.csv")

st.subheader("📄 Data Preview")
st.dataframe(df.head(20))

st.subheader("📊 Protocol Distribution")
st.bar_chart(df["protocol"].value_counts())

st.subheader("🚨 Anomaly Overview")
anomalies = df[df["anomaly"] == -1]
st.write(f"Detected {len(anomalies)} anomalies")
st.dataframe(anomalies)
