-- ایجاد دیتابیس با نام bismark_servicenet_db
-- تنظیم charset به utf8mb4 برای پشتیبانی کامل از یونیکد (شامل فارسی و ایموجی)
-- تنظیم collation به utf8mb4_unicode_ci برای ترتیب و مقایسه درست رشته‌ها
CREATE DATABASE bismark_servicenet_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ایجاد یوزر جدید با نام 'servicenet_admin' و رمز عبور مشخص
-- این یوزر فقط از localhost می‌تواند به سرور متصل شود
CREATE USER 'servicenet_admin'@'localhost' IDENTIFIED BY 'StrongBismarkPass!2025';

-- اعطای تمامی دسترسی‌ها (خواندن، نوشتن، تغییر ساختار و ...) به یوزر روی دیتابیس bismark_servicenet_db
GRANT ALL PRIVILEGES ON bismark_servicenet_db.* TO 'servicenet_admin'@'localhost';

-- بارگذاری مجدد دسترسی‌ها برای اعمال تغییرات بالا
FLUSH PRIVILEGES;


pip install Flask Flask-SQLAlchemy



