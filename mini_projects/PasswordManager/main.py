import connection
import os
import time
from password_maneger import Manager


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
    return Manager(login, password, key)


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


def clear_screen():
    if os.name == 'nt':  # If the OS is Windows
        os.system('cls')
    else:  # Otherwise (assume Unix-like)
        os.system('clear')


if __name__ == "__main__":
    main()
