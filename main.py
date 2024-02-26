# main.py

import streamlit as st
import requests

st.write("세차장 키오스크 MQTT REST API 테스트")

# EMQ X MQTT 서비스의 HTTP API URL
mqtt_api_endpoirnt = st.secrets["API_ENDPOINT"]
api_url = mqtt_api_endpoirnt

headers = {
    'Content-Type': 'application/json',
}


# 메시지 전송 함수
def send_mqtt_message(topic, message):
    data = {
        "topic": topic,
        "payload": message,
        "qos": 0,  # QoS level
        "retain": False,  # Retain flag
        "client_id": "otacosystem0221"  # Client ID
    }

    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        st.success(f"Message sent to {topic}!")
    else:
        st.error("Failed to send message.")


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
