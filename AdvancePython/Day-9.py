# Day 9: Database Handling

# Task 2:
import mysql.connector

conn = mysql.connector.connect(
    user="root", host="localhost", passwd="", database="test"
)

cursor = conn.cursor()

records = """CREATE TABLE EMPLOYEE(
NAME CHAR(20) NOT NULL,
AGE INT,
CITY CHAR(30)
)"""

cursor.execute(records)
conn.close()
