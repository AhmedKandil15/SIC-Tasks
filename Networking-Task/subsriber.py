import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "topic/temperature"


def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
