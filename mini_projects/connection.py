import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='wagner25',
    database='password_manager'
)

mycursor = mydb.cursor()
