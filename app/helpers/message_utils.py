def extract_text(data: dict) -> str:
    """
    استخراج متن پیام از داده دریافتی وبهوک
    """
    return data.get('body') or data.get('message') or ''

def is_valid_message(data: dict) -> bool:
    """
    بررسی اعتبار داده پیام (وجود شماره و متن)
    """
    phone = data.get('from') or data.get('sender')
    message = extract_text(data)
    return bool(phone and message)
