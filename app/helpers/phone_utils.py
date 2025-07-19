
def normalize_phone(phone: str) -> str:
    """
    نرمالایز کردن شماره تلفن برای استفاده یکنواخت در کل پروژه
    (مثلا حذف +98 و تبدیل به 09...)
    """
    if phone.startswith('+98'):
        return '0' + phone[3:]
    elif phone.startswith('98'):
        return '0' + phone[2:]
    return phone
