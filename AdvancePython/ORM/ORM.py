import os
from mongoengine import connect, Document, StringField

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

if not all([host, port, db_name]):
    raise ValueError("MONGO_URI not found! Ensure you started with F5.")

connection_string = f"mongodb://{host}:{port}/{db_name}"

print(f"--- Connecting to: {connection_string} ---")
connect(host=connection_string)


class User(Document):
    name = StringField(required=True)
    email = StringField(unique=True)


try:
    users = User.objects
    if not users:
        print("Connected, but no users found in the collection.")
    for user in users:
        print(f"Found user: {user.name}")
except Exception as e:
    print(f"Connection failed: {e}")
