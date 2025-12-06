import paho.mqtt.client as mqtt
import time
import random
import json

# MQTT Broker IP (Home Assistant)
broker = "192.168.1.7"
topic = "home/HardhikT-2025/sensor"

# Connect to MQTT
client = mqtt.Client()
client.connect(broker)

print("\nMQTT Sensor Started... Sending Data Every 5 Seconds.\n")

while True:
    # Simulated values
    temp = random.randint(20, 35)
    hum = random.randint(40, 80)
    motion = random.randint(0, 1)  # <-- IMPORTANT: motion now defined BEFORE using

    payload = {
        "name": "Hardhik Thummala",
        "reg": "42732083",
        "temp": temp,
        "hum": hum,
        "motion": motion
    }

    client.publish(topic, json.dumps(payload))   # Sending proper JSON format
    print(f"Published → {payload}")

    time.sleep(5)
