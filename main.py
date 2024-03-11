import json
import streamlit as st
import paho.mqtt.client as mqtt
import requests

# API Endpoint가 Streamlit secrets에 저장되어 있다고 가정합니다.
# 예를 들어 secrets.toml 파일에 api_endpoint="https://example.com/api/v1" 형태로 저장합니다.
api_endpoint = st.secrets["API_ENDPOINT"]
app_id = st.secrets["APP_ID"]
app_secret = st.secrets["APP_SECRET"]

mqtt_broker = "your_mqtt_broker_address"
mqtt_port = 1883  # Default MQTT port if not using SSL/TLS
mqtt_topic = "your_topic"

# 스트림릿 앱의 UI를 구성합니다.
st.title('메시지 전송 웹앱')

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)


if st.button('수신'):
    url = f'{api_endpoint}/subscriptions'
    auth = (app_id, app_secret)
    headers = {'Content-Type': 'application/json'}

    response = requests.get(url, auth=(app_id, app_secret), headers=headers)

    if response.ok:
        message_data = response.json()
        st.success('메시지를 성공적으로 수신하였습니다.')
        st.json(message_data)
    else:
        st.error('메시지를 수신하는데 실패했습니다.')


if st.button('전송'):
    message = "Hello, MQTT!"
    client.publish(mqtt_topic, message)
    st.success('Message sent successfully!')


if st.button('구독'):
    url = f'{api_endpoint}/clients/otacosystem_client_1/subscribe'
    auth = (app_id, app_secret)
    headers = {'Content-Type': 'application/json'}
    data = {"topic": "otacosystem/carwash", "qos": 1}

    response = requests.post(url, auth=auth, headers=headers, json=data)

    if response.ok:
        st.success('구독이 성공적으로 완료되었습니다.')
        st.json(response.json())
    else:
        st.error('구독을 실패했습니다. 에러 메시지: ' + response.text)


if st.button('모든 클라이언트 보기'):
    url = f'{api_endpoint}/clients'
    auth = (app_id, app_secret)
    params = {
        '_page': 1,
        '_limit': 50
    }
    response = requests.get(url, auth=auth, params=params)

    if response.ok:
        st.success('클라이언트 정보 조회에 성공했습니다. 🎉')
        st.json(response.json())
    else:
        st.error('정보 조회에 실패했습니다. 😢 에러 메시지: ' + response.text)
