import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'

    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_DB_URL') or \
        'mysql+pymysql://bismark_support:StrongPassword123!@localhost/bismark_servicenet_db'

    params = quote_plus(
        "DRIVER={ODBC Driver 11 for SQL Server};"
        "SERVER=RAHIN97\\MAHAK;"
        "DATABASE=mahak;"
        "UID=sa;"
        "PWD=Aa123456;"
    )
    SQLALCHEMY_BINDS = {
        'mahak': f"mssql+pyodbc:///?odbc_connect={params}"
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False

    WPP_API_BASE_URL = os.environ.get("WPP_API_BASE_URL") or "http://localhost:21465/api"
    WPP_SESSION_NAME = os.environ.get("WPP_SESSION_NAME") or "mySession"
    WPP_SESSION_TOKEN = os.environ.get("WPP_SESSION_TOKEN") or "$2b$10$8sdQhP86c6QsfOCI3set4ugI2gadgnHB6KzD0MSIGt6Z5FGVlpRXO"

    DATA_SOURCE_MODE = os.environ.get('DATA_SOURCE_MODE') or 'remote'
