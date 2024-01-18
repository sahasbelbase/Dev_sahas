# config.py
from urllib.parse import quote_plus

# Use Windows Authentication
SQLALCHEMY_DATABASE_URI = (
    'mssql+pyodbc://'
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-DUJEM16\SQLEXPRESS;'
    'DATABASE=Hotel_Reservation_System;'
    'Trusted_Connection=yes;'
)

# Disable SQLAlchemy modification tracking
SQLALCHEMY_TRACK_MODIFICATIONS = False
