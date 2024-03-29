class Player:
    def __init__(self, name: str, age: str):
        self.name = name
        while not age.isdigit():
            print("\nOnly digits are allowed")
            age = str(input("What is the age of the player: "))
        self.age = int(age)

    def check_age(self):
        if self.age >= 18:
            print(f"{self.name}, you are an adult")
        elif 18 > self.age >= 13:
            print(f"{self.name}, you are an adolecent")
        else:
            print(f"{self.name}, you are an child")


def main():
    num = int(input("How many players do you want to add: "))
    for i in range(num):
        p = Player(str(input("Name: ")), str(input("Age: ")))
        p.check_age()


if __name__ == "__main__":
    main()
