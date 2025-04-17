import mysql.connector

def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kusuma@12",
            database="revstock_db"
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None