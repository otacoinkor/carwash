# mqtt_client.py
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.emqx.io"  # "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "otaco_sys"

user_data = {"is_connected": False}


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # 연결 상태 업데이트
    userdata["is_connected"] = True


# Define on_disconnect callback
def on_disconnect(client, userdata, rc):
    print("Disconnected")
    # 연결 해제 상태 업데이트
    userdata["is_connected"] = False


def create_mqtt_client(userdata):
    client = mqtt.Client(userdata=user_data)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    return client


def send_mqtt_message(client, message):
    client.publish(MQTT_TOPIC, message)
