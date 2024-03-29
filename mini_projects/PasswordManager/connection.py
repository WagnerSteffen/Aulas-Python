import mysql.connector


def create_database_and_tables():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host="localhost", user="root", password=str(input("Password: "))
    )

    # Create the database if it doesn't exist
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS password_manager")
    cursor.execute("USE password_manager")

    # Create the profiles table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS profiles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user VARCHAR(255),
            password VARBINARY(255)
        )
    """
    )

    # Create the records table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS records (
            domain VARCHAR(100),
            login TEXT,
            password TEXT,
            user INT
        )
    """
    )

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()


create_database_and_tables()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=str(input("Password: ")),
    database="password_manager",
)
mycursor = mydb.cursor()
