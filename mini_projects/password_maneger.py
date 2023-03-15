import connection


class manager:
    def __init__(self, user, password, encription) -> None:
        self.__user = user
        self.__password = password
        self.__encryption = encription
        connection.mycursor.execute(f"""INSERT INTO profiles (user, password)
                                    SELECT * FROM (SELECT '{self.__user}', AES_ENCRYPT('{self.__password}','{self.__encryption}'
                                    )) AS tmp
                                    WHERE NOT EXISTS (
                                        SELECT user FROM profiles WHERE user = '{self.__user}'
                                    ) LIMIT 1;""")
        print(connection.mycursor.rowcount, 'rows affected')
        connection.mydb.commit()
    def listit(self):
        #return a list of domain to see password
        pass
    def view(self, domain):
        #view the password of the selected domain
        pass
    def create(self, door, lock, key):
        #create a new record in the database
        self.__domain = door
        self.__login = lock
        self.__key = key
        connection.mycursor.execute(f"""
                                    INSERT INTO records(user, password, domain)
                                    VALUES("{lock}", "{key}", "{door}")""")
        connection.mydb.commit()
        print(connection.mycursor.rowcount, "record inserted.")
        
    def remove(self, door):
        #remove the record of that domain
        connection.mycursor.execute(f"""
                                    DELETE FROM records WHERE domain LIKE "{door}" """)
        connection.mydb.commit()
        print(connection.mycursor.rowcount, "deleted rows")

teste = manager('wagner', 'teste','encription')
#teste.create('Google', 'teste', 'thisisapassword')
#teste.remove("Google")