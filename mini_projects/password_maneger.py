import connection
import os
import time

def clear_screen():
    if os.name == 'nt':  # If the OS is Windows
        os.system('cls')
    else:  # Otherwise (assume Unix-like)
        os.system('clear')
class manager:
    def __init__(self, user, password, encription) -> None:
        self.user = user
        self.__password = password
        self.__encryption = encription
    def create_account(self):
        connection.mycursor.execute(f"""INSERT INTO profiles (user, password)
                                    SELECT * FROM (SELECT '{self.user}', AES_ENCRYPT('{self.__password}','{self.__encryption}'
                                    )) AS tmp
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
        #return a list of domain to see password
        query = f""" SELECT domain FROM records WHERE user = {self.__id} """
        connection.mycursor.execute(query)
        domains = connection.mycursor.fetchall()
        print("Here is the list")
        for i, t in enumerate(domains):
            print(i, t[0].title())
    def view(self, domain):
        #view the password of the selected domain
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
        #create a new record in the database
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
        #remove the record of that domain
        connection.mycursor.execute(f"""
                                    DELETE FROM records WHERE domain LIKE "{door}" """)
        connection.mydb.commit()
        print(connection.mycursor.rowcount, "deleted rows")

def main():
    while True:
        option = int(input("1 - Create Profile\n2 - Access account\n0 - Exit\n:"))
        if option == 0:
            connection.mycursor.close()
            connection.mydb.close()
            break
        elif option == 1:
            account = profile()
            account.create_account()
            clear_screen()
        elif option == 2:
            account = profile()
            while account.access_account() is False and account.user != "":
                clear_screen()
                print("Access denied!")
                account = profile()
            if account.user == "":
                break
            elif account.access_account():
                clear_screen()
                print("Access granted!")
                records_options(account)
        else:
            print("Choose between 1, 2 and 3. Only digits!")
    connection.mycursor.close()
    print("See you soon!")
    time.sleep(1)

def profile():
    login = str(input("Login: "))
    password = str(input("Password: "))
    key = str(input("Encryption key: "))
    return manager(login, password, key)

def records_options(user):
    while True:
        record_option = int(input(
    """
    What do you wish to do?
    1 - View what is save
    2 - View password
    3 - Create new record
    4 - Delete record
    0 - Exit
    : """))
        if record_option == 1:
            clear_screen()
            user.listit()
        elif record_option == 2:
            domain = str(input("What is the domain of the password?\n:"))
            clear_screen()
            user.view(domain)
        elif record_option == 3:
            domain = str(input("What is the domain of the password?\n:"))
            login = str(input("What is the login?\n:"))
            password = str(input("What is the the password?\n:"))
            user.create(domain, login, password)
            time.sleep(1)
            clear_screen()
        elif record_option == 4:
            domain = str(input("What is the domain of record that you want to remove?\n:"))
            user.remove(domain)
            time.sleep(1)
            clear_screen()
        elif record_option == 0:
            break
        else:
            print("Only number, please!")
if __name__ == "__main__":
    main()