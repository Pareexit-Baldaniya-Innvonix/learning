import mysql.connector

DB_INFO = "AdvancePython/Day-9 Database Handling/.env"

with open(DB_INFO) as f:
    config = dict(
        line.strip().split("=", 1)
        for line in f
        if "=" in line and not line.startswith("#")
    )


try:
    conn = mysql.connector.connect(
        host=config["DB_HOST"], user=config["DB_USER"], password=config["DB_PASSWORD"]
    )
    print(f"Connected successfully!")
except KeyError as e:
    print(f"Missing key in .env: {e}")
