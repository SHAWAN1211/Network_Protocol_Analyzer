🛡️ Network Protocol Analyzer with Machine Learning Insights

A Python-based real-time network packet analyzer that uses machine learning to detect suspicious traffic. Built for educational and research purposes, this project captures live packets, extracts features, trains a model, and identifies anomalies in network behavior.

 🚀 Features

- ✅ Real-time packet sniffing using Scapy
- ✅ Feature extraction from live network traffic
- ✅ Machine learning-based anomaly detection (Isolation Forest)
- ✅ Data visualization with Matplotlib and Seaborn
- ✅ Streamlit-based interactive dashboard

 📂 Project Structure

network\_analyzer\_ml/
│
├── capture.py              # Captures live packets
├── extract\_features.py     # Converts captured packets to ML features
├── train\_model.py          # Trains the anomaly detection model
├── detect.py               # Detects anomalous packets
├── visualize.py            # Graphs protocol usage and anomalies
├── dashboard.py            # Launches an interactive dashboard
│
├── dataset/                # Stores captured\_data.csv and features.csv
├── models/                 # Stores the trained model (isolation\_forest.pkl)
├── results/                # Stores results of anomaly detection



 💻 Requirements

- Python 3.x
- pip
- Admin privileges (for packet sniffing)
- [Npcap](https://nmap.org/npcap/) (WinPcap-compatible mode)

 📦 Python Libraries:

bash:

pip install scapy pandas matplotlib seaborn scikit-learn joblib streamlit


🏁 Getting Started

 1. Capture packets

⚠️ Run VS Code or terminal as administrator.

bash:
python capture.py


Press "CTRL+C" to stop capturing.


2. Extract features

bash:
python extract_features.py

3. Train the ML model

bash:
python train_model.py


4. Detect anomalies

bash:
python detect.py


5. Visualize graphs (optional)

bash:
python visualize.py


6. Run Streamlit Dashboard (optional)

bash:
streamlit run dashboard.py

📊 How It Works

| Stage           | Description                                   |
| --------------- | --------------------------------------------- |
| Packet Capture  | Uses "scapy.sniff()" to collect live packets  |
| Feature Extract | Pulls protocol and length data from packets   |
| ML Model        | Trains Isolation Forest on clean traffic      |
| Detection       | Labels new packets as normal or anomalous     |
| Dashboard       | Displays raw data, protocol stats, and alerts |



🔐 Permissions Note

* On **Windows**, install [Npcap](https://nmap.org/npcap/) and run scripts **as Administrator**.
* On **Linux**, use "sudo" for "apture.py".


📸 Screenshots

![image](https://github.com/user-attachments/assets/da01aa16-f861-4f84-b8c9-9e518f7e5317)

![image](https://github.com/user-attachments/assets/d84338f5-f6da-4014-b39a-508a1da555d9)

![image](https://github.com/user-attachments/assets/882912f1-c439-4859-bd59-f137bfe49461)

![image](https://github.com/user-attachments/assets/aff142d4-50a5-402b-a590-230645e36844)

![image](https://github.com/user-attachments/assets/8ecc49cd-bce1-472c-b5c3-784429561ed7)

📚 Learning Outcomes

 🧠 Understanding of network packet structure (IP, TCP, UDP)
 
 🤖 Use of unsupervised machine learning for anomaly detection
 
 📈 Visualizing network patterns and threats in real-time

🙌 Acknowledgements

* [Scapy](https://scapy.net/)
* [Scikit-learn](https://scikit-learn.org/)
* [Streamlit](https://streamlit.io/)
* [Npcap](https://nmap.org/npcap/)




