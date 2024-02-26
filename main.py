# main.py

import streamlit as st
from gmqtt import Client as MQTTClient


st.write("세차장 키오스크 MQTT 테스트 Paho ")

# MQTT 클라이언트 객체 생성 및 연결
mqtt_broker = st.secrets["MQTT_BROKER"]

client = MQTTClient("otaco_sys_0221")
client.connect(mqtt_broker)


def send_mqtt_message(topic, message):
    # 주어진 토픽에 메시지 발행
    client.publish(topic, message)


# Streamlit 앱
st.title('MQTT Message Sender')

if st.button("Send Message 1"):
    send_mqtt_message("topic1", "Hello, Streamlit 1!")
    st.success("Message 1 sent!")

if st.button("Send Message 2"):
    send_mqtt_message("topic2", "Hello, Streamlit 2!")
    st.success("Message 2 sent!")

if st.button("Send Message 3"):
    send_mqtt_message("topic3", "Hello, Streamlit 3!")
    st.success("Message 3 sent!")
