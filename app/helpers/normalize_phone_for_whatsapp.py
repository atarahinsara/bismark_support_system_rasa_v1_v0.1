def normalize_phone_for_whatsapp(phone: str) -> str:
    """
    Normalize a WhatsApp phone number by:
    - Removing suffixes like '@c.us'
    - Removing spaces, dashes, etc.
    - Making sure it's numeric
    """
    if not phone:
        return ''
    
    # Remove domain suffix
    if '@' in phone:
        phone = phone.split('@')[0]
    
    # Remove non-numeric characters
    phone = ''.join(filter(str.isdigit, phone))
    
    return phone
