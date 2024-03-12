from datetime import datetime

import streamlit as st
import paho.mqtt.client as mqtt

mqtt_broker = "s2de96e2.ala.asia-southeast1.emqxsl.com"  # "broker.hivemq.com"
mqtt_port = 8883  # 1883
mqtt_topic = "otaco_sys"

# 스트림릿 앱의 UI를 구성합니다.
st.title('세차장 MQTT 테스트')

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)

if st.button('전송'):
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    print(time_string)

    message = "MQTT 테스트 " + time_string
    client.publish(mqtt_topic, message)

    st.success('Message sent successfully!')
