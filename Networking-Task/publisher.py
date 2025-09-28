import paho.mqtt.client as mqtt
import time
import random

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "topic/temperature"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()

while True:
    temp = random.randint(0, 50)
    client.publish(TOPIC, temp)
    print(f"Published: {temp}")
    time.sleep(2)
