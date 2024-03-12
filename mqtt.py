# mqtt.py
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.emqx.io"  # "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "otaco_sys"


# Define on_connect callback
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


# Define on_disconnect callback
def on_disconnect(client, userdata, rc):
    print("Disconnected")


def create_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    return client


def send_mqtt_message(client, message):
    client.publish(MQTT_TOPIC, message)
