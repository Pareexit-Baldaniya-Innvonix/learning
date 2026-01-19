# Day 9: Database Handling

# Task 1: 
# -> database is a collection of data which is stored electronically
# -> managed by DBMS allows user to do CRUD operations
# -> two types:

# 1. Relational databases(RDBMS):
# -> MySQL, PostgreSQL, SQLite
# -> stores data in tables as row and column
# -> all data connected through keys, enables JOIN operations
# -> slower
# -> prioritize ACID(Atomicity, Consistency, Isolation, Durability) for accuracy 
# -> store in binary file format

# 2. Non-Relational databases(NoSQL):
# -> MongoDB, Cassandra
# -> stores data in documents, key-value pairs, wide column and graphs
# -> dynamic, each record has different structure
# -> no database JOINs are there
# -> faster
# -> prioritize BASE(Basically Available, Soft state, Eventual consistency) for speed and availability
# -> store in json file format

# Task 2:
import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    passwd = "",
    database = "test"
)

cursor = conn.cursor()

records = """CREATE TABLE EMPLOYEE(
NAME CHAR(20) NOT NULL,
AGE INT,
CITY CHAR(30)
)"""

cursor.execute(records)
# cursor.execute("SHOW TABLES")

# print("-- Tables in database --")
# for table in cursor:
#     print(table)
    
conn.close()


# mysql -u root -p --> for connecting to the MySQL  ## here pass is only pressing 'enter' key
# -> show databaseS; --> for checking all available databases
# -> show tables; --> for checking all available tables in database
# -> status; --> for full info of database
# -> use database_name --> for switch to that database
# -> select * from database_name; --> for getting all tables


# different ways to delete database:
# 1. manual:
# -> DROP DATABASE DATABASE_NAME;  --> quick terminal work
# -> DROP DATABASE IF EXISTS DATABASE_NAME
# -> directly delete through the terminal

# 2. programmatic:
# -> cursor.execute("DROP DATABASE IF EXISTS DATABASE_NAME")  --> automation
# -> uses a connector library to delete database through script
# -> automatically delete the database

# 3. shell utility:
# -> mysqladmin -u root -p drop database_name  --> quick deletion usind linux cmd
# -> also delete database through terminal but ask before proceeding
# -> delete database without entering into mysql