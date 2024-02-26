import json

import streamlit as st
import requests

# API Endpoint가 Streamlit secrets에 저장되어 있다고 가정합니다.
# 예를 들어 secrets.toml 파일에 api_endpoint="https://example.com/api/v1" 형태로 저장합니다.
api_endpoint = st.secrets["API_ENDPOINT"]
app_id = st.secrets["APP_ID"]
app_secret = st.secrets["APP_SECRET"]

# 스트림릿 앱의 UI를 구성합니다.
st.title('메시지 전송 앱')

# API 요청을 보낼 준비를 합니다.
url = f'{api_endpoint}/subscriptions'  # 실제 엔드포인트를 사용합니다.
auth = (app_id, app_secret)  # 사용자 ID와 비밀번호

# GET 요청을 보내 구독 정보를 요청합니다.
response = requests.get(url, auth=auth)

# 응답을 확인하여 화면에 출력합니다.
if response.ok:
    # 응답 데이터를 JSON 형태로 변환합니다.
    subscriptions = response.json()
    st.success('구독 정보를 성공적으로 수신하였습니다.')
    # 구독 정보를 화면에 표시합니다 (예시)
    st.json(subscriptions)
else:
    st.error('구독 정보를 수신하는데 실패하였습니다.')

# 사용자로부터 데이터를 입력받습니다.
# message = st.text_input('메시지를 입력하세요')

# '전송' 버튼을 만듭니다.
if st.button('전송'):
    # API 요청을 보낼 준비를 합니다.
    url = f'{api_endpoint}/publish'  # api_endpoint에 해당하는 실제 엔드포인트를 사용합니다.
    auth = (app_id, app_secret)  # 사용자 이름과 비밀번호
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"topic": "t/a", "qos": 1, "payload": "Hello EMQX"})

    # POST 요청을 보내 메시지를 전송합니다.
    response = requests.post(url, auth=auth, headers=headers, data=data)

    # 응답을 확인하여 화면에 출력합니다.
    if response.ok:
        st.success('메시지가 성공적으로 전송되었습니다.')
    else:
        st.error('메시지를 전송하는데 실패했습니다.')

# Streamlit 앱을 실행하려면 위 코드를 streamlit_app.py 파일로 저장하고
# 스트림릿을 실행합니다.
