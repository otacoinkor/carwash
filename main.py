# main.py
#
# streamlit run Z:\work\python\carwash\main.py

from datetime import datetime
import streamlit as st
from mqtt_client import create_mqtt_client, send_mqtt_message

# 스트림릿 앱의 UI를 구성합니다.
st.title('otaco MQTT 테스트')

if 'mqtt_userdata' not in st.session_state:
    st.session_state.mqtt_userdata = {"is_connected": False}


# MQTT 클라이언트 초기화 및 연결을 관리하는 함수
def init_mqtt_client():
    print(st.session_state)

    if st.session_state.mqtt_userdata['is_connected']:
        st.write("MQTT 기존 연결 사용")
    else:
        st.session_state.mqtt_client = create_mqtt_client(st.session_state.mqtt_userdata)
        st.write("MQTT 연결 성공")


# MQTT 클라이언트 초기화
init_mqtt_client()

if st.button('전송'):
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    print(time_string)

    message = "MQTT 테스트 " + time_string
    send_mqtt_message(st.session_state.mqtt_client, message)

    st.success('Message sent successfully!')
