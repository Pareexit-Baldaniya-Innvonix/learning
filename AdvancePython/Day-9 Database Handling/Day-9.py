import mysql.connector
import os

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

missing_keys = [k for k, v in db_config.items() if v is None]
if missing_keys:
    raise ValueError(
        f"Missing environment variables: {', '.join(missing_keys)}. Remember to run with F5!"
    )


try:
    conn = mysql.connector.connect(**db_config)
    print(f"Connected successfully!")
    conn.close()
except mysql.connector.Error as e:
    print(f"Error: {e}")
