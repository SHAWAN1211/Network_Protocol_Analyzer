from scapy.all import sniff, IP
import csv
from datetime import datetime
import os

os.makedirs("dataset", exist_ok=True)
file_path = "dataset/captured_data.csv"

if not os.path.exists(file_path):
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "src_ip", "dst_ip", "protocol", "length"])

def process_packet(packet):
    if IP in packet:
        proto = packet.proto
        src = packet[IP].src
        dst = packet[IP].dst
        length = len(packet)
        timestamp = datetime.now()
        with open(file_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, src, dst, proto, length])

print("🟢 Sniffing started... Press CTRL+C to stop.")
sniff(prn=process_packet, store=False)
