# main.py

import streamlit as st
import paho.mqtt.client as mqtt

st.write("세차장 키오스크 MQTT REST API 테스트")

# MQTT 클라이언트 객체 생성 및 연결
client = mqtt.Client("otaocotest0221")
client.connect(host=st.secrets["MQTT_BROKER"], port=8883, keepalive=60)
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
