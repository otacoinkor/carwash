# main.py

import paho.mqtt.client as mqtt
import streamlit as st


st.write("세차장 키오스크 MQTT 테스트 Paho ")

# MQTT 클라이언트 객체 생성 및 연결
client = mqtt.Client()
client.connect(st.secrets["MQTT_BROKER"], 8883, 60)
client.loop_start()


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
