import dbm
import os
import time
db = dbm.open('sites.db', 'c')

def main():   # sourcery skip: extract-duplicate-method, switch
    while True:
        options = int(input("""
    What you wish to do?
    1 - View websites saved
    2 - Save a new website
    3 - Remove website
    0 - Exit
    """))
        if options == 0:
            break
        elif options == 1:
            clear_screen()
            print('Here is the list:')
            for key, value in enumerate(db.keys()):
                print(key, value.decode().title(), ' -> ', db[value].decode())
        elif options == 2:
            domain = str(input("What is the name of the website:\n")).lower()
            site = str(input("Digit the website: ")).lower()
            site = check_website(site)
            db[domain] = site.encode()
            print('Website recorded!')
            time.sleep(1)
            clear_screen()
        elif options == 3:
            domain = str(input("What is the domain that you wish to remove?\n")).lower().encode()
            if domain in db.keys():
                db.pop(domain)
                print('Domain successfully removed!')
            else:
                print("This domain is not avalible, please select one of the below:\n")
                for key, value in enumerate(db.keys()):
                    print(key, value.decode().title(), ' -> ', db[value].decode())
            time.sleep(1)
            clear_screen()
        else:
            print("Only numbers, please!")
            time.sleep(1)
            clear_screen()

    db.close()

def check_website(website:str):
    section = website.split('.')
    if section[0] != 'www':
        section.insert(0, 'www')
    while 'com' not in section:
        warning = str(input('Note: Your website its missing the ".com", thats right?\n')).lower()
        if warning.startswith('n'):
            site = str(input("Digit the website: "))
        else:
            site = website
            break
        section = site.split('.')
    return '.'.join(section)


def clear_screen():
    if os.name == 'nt':  # If the OS is Windows
        os.system('cls')
    else:  # Otherwise (assume Unix-like)
        os.system('clear')

if __name__ == "__main__":
    main()