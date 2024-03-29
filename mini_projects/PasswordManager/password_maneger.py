import connection

class Manager:
    def __init__(self, user, password, encription) -> None:
        self.__id = None
        self.__key = None
        self.__login = None
        self.__domain = None
        self.user = user
        self.__password = password
        self.__encryption = encription

    def create_account(self):
        connection.mycursor.execute(f"""INSERT INTO profiles (user, password)
                                    SELECT * FROM (SELECT '{self.user}', AES_ENCRYPT('{self.__password}',
                                    '{self.__encryption}')) AS tmp
                                    WHERE NOT EXISTS (
                                        SELECT user FROM profiles WHERE user = '{self.user}'
                                    ) LIMIT 1;""")
        print(connection.mycursor.rowcount, 'rows affected')
        connection.mydb.commit()

    def access_account(self):
        # sourcery skip: boolean-if-exp-identity, remove-unnecessary-cast
        query = f""" SELECT id FROM profiles WHERE user = '{self.user}' 
                AND password = AES_ENCRYPT('{self.__password}','{self.__encryption}') """
        connection.mycursor.execute(query)
        access = connection.mycursor.fetchone()
        access = access[0] if access is not None else None
        self.__id = access
        return True if access is not None else False

    def listit(self):
        # return a list of domain to see password
        query = f""" SELECT domain FROM records WHERE user = {self.__id} """
        connection.mycursor.execute(query)
        domains = connection.mycursor.fetchall()
        print("Here is the list")
        for i, t in enumerate(domains):
            print(i, t[0].title())

    def view(self, domain):
        # view the password of the selected domain
        query = f""" SELECT domain, login, password FROM records WHERE user = {self.__id} AND domain = '{domain}' """
        connection.mycursor.execute(query)
        view = connection.mycursor.fetchall()
        print(f"""
Here is your information for {view[0][0].title()}
Login: {view[0][1]}
Password: {view[0][2]} 
"""
              )

    def create(self, door, lock, key):
        # create a new record in the database
        self.__domain = door
        self.__login = lock
        self.__key = key
        connection.mycursor.execute(f"""
                                    INSERT INTO records(login, password, domain, user)
                                    VALUES("{lock}", "{key}", "{door}", {self.__id})
                                    ON DUPLICATE KEY UPDATE login = "{lock}", password = "{key}" """)
        connection.mydb.commit()
        print(connection.mycursor.rowcount, "record inserted.")

    def remove(self, door):
        # remove the record of that domain
        connection.mycursor.execute(f"""
                                    DELETE FROM records WHERE domain LIKE "{door}" """)
        connection.mydb.commit()
        print(connection.mycursor.rowcount, "deleted rows")



