from flask import Blueprint, request, jsonify
from app.helpers.normalize_phone_for_whatsapp import normalize_phone_for_whatsapp
from app.helpers.wppconnect_api import send_message_to_user

webhook_bp = Blueprint('webhook', __name__)
message_counts = {}

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
   # print("📥 دریافت اطلاعات خام:", data)

    event_type = data.get('event')
    if event_type != 'onmessage':
        print(f"⛔️ رویداد غیر پیام: {event_type} — نادیده گرفته شد.")
        return jsonify({'status': 'ignored', 'event': event_type}), 200

    raw_phone = data.get('from') or data.get('sender')
    message_text = data.get('body') or data.get('message')

    if not raw_phone or not message_text:
        print(f"❌ شماره یا پیام ناقص است. داده‌ها: {data}")
        return jsonify({'error': 'Missing phone or message'}), 400

    # نرمال‌سازی شماره
    phone = normalize_phone_for_whatsapp(raw_phone)

    # شمارش پیام‌ها
    message_counts[phone] = message_counts.get(phone, 0) + 1

    print(f"✅ پیام از {phone}: {message_text}")
    print(f"📊 تعداد پیام‌های این شماره: {message_counts[phone]}")

    # پاسخ برای کاربر ارسال شود
    response_message = f"سلام! پیام شما دریافت شد ✅\nمتن شما: {message_text}"
    send_message_to_user(phone, response_message)

    return jsonify({
        'status': 'success',
        'phone': phone,
        'message': message_text,
        'count': message_counts[phone]
    }), 200
