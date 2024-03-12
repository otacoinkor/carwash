from datetime import datetime
import streamlit as st
from mqtt import create_mqtt_client, send_mqtt_message

# 스트림릿 앱의 UI를 구성합니다.
st.title('otaco MQTT 테스트')

mqtt_client = create_mqtt_client()

if st.button('전송'):
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    print(time_string)

    message = "MQTT 테스트 " + time_string
    send_mqtt_message(mqtt_client, message)

    st.success('Message sent successfully!')
