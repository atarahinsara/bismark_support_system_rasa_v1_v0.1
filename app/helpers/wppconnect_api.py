import requests
from flask import current_app

def send_message_to_user(phone: str, message: str) -> dict:
    """
    ارسال پیام به شماره با استفاده از API WPPConnect
    """
    base_url = current_app.config['WPP_API_BASE_URL']
    token = current_app.config['WPP_SESSION_TOKEN']
    session_name = current_app.config['WPP_SESSION_NAME']

    url = f"{base_url}/{session_name}/send-message"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "phone": phone,
        "message": message
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
