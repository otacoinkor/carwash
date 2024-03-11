
import streamlit as st
import paho.mqtt.client as mqtt

mqtt_broker = "your_mqtt_broker_address"
mqtt_port = 1883  # Default MQTT port if not using SSL/TLS
mqtt_topic = "your_topic"

# 스트림릿 앱의 UI를 구성합니다.
st.title('메시지 전송 웹앱')

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)

if st.button('전송'):
    message = "Hello, MQTT!"
    client.publish(mqtt_topic, message)
    st.success('Message sent successfully!')


