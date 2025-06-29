#Task 1. Let's Build Your Database: Your Gateway to Data Adventure!

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connecting to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',         # Update with your username
            password='password'  # Update with your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: Unable to connect or create database.\nDetails: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database(
