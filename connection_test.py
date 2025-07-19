'''
import pyodbc

# تعریف رشته اتصال
conn_str = (
    "DRIVER={ODBC Driver 11 for SQL Server};"
    "SERVER=RAHIN97\MAHAK;"  # یا اگر با نام خاصی هست مثل DESKTOP-123\SQLEXPRESS
    "DATABASE=mahak;"
    "UID=sa;"
    "PWD=Aa123456;"
)

try:
    conn = pyodbc.connect(conn_str)
    print("✅ اتصال برقرار شد.")
except Exception as e:
    print("❌ خطا در اتصال:", e)



import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='bismark_support',
        password='StrongPassword123!',
        database='bismark_servicenet_db'
    )
    with connection.cursor() as cursor:
        cursor.execute('SELECT 1')
        result = cursor.fetchone()
        print('اتصال موفق، نتیجه:', result)
    connection.close()
except Exception as e:
    print('خطا در اتصال:', e)
'''

from sqlalchemy.engine.url import make_url

def test_mysql_connection():
    try:
        db_url = make_url(Config.SQLALCHEMY_DATABASE_URI)

        connection = pymysql.connect(
            host=db_url.host,
            user=db_url.username,
            password=db_url.password,
            database=db_url.database
        )
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            result = cursor.fetchone()
            print('✅ اتصال به MySQL موفق، نتیجه:', result)
        connection.close()
    except Exception as e:
        print('❌ خطا در اتصال به MySQL:', e)
