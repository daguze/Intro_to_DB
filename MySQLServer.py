import mysql.connector

def create_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dzeme@1832!"
        )
        if conn.is_connected():
            print("Connected to MySQL Server successfully!")
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            conn.close()
if __name__ == "__main__":
    create_database()