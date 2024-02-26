# main.py

import streamlit as st
import random
from paho.mqtt import client as mqtt_client
import threading

st.write("세차장 키오스크 MQTT REST API 테스트")

broker = 'broker.emqx.io'
port = 8883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = '1234567890'

# Streamlit 앱
st.title('MQTT Message Sender')


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        st.write("Connected to MQTT Broker!")
    else:
        st.write("Failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):
    st.write(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")


def connect_mqtt() -> mqtt_client:
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()


if st.button('Start MQTT Client'):
    threading.Thread(target=run).start()
