from datetime import datetime
import streamlit as st
import paho.mqtt.client as mqtt
import threading

MQTT_BROKER = "broker.emqx.io"  # "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "otaco_sys"


# Define on_connect callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        st.write("Connected to MQTT Broker!")
    else:
        st.write("Failed to connect, return code %d\n", rc)


# Define on_disconnect callback
def on_disconnect(client, userdata, rc):
    if rc != 0:
        st.write("Unexpected disconnection.")


def mqtt_connect():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    return client


# 스트림릿 앱의 UI를 구성합니다.
st.title('MQTT 테스트')

mqtt_client = mqtt_connect()

if st.button('전송'):
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    print(time_string)

    message = "MQTT 테스트 " + time_string
    mqtt_client.publish(MQTT_TOPIC, message)

    st.success('Message sent successfully!')
