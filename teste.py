def create_player() -> [str, str]:
    name: str = str(input("\nDigite o nome do jogador: "))
    age: str = str(input("Digite a idade do jogador: "))
    while not age.isdigit():
        print("\nOnly digits are allowed")
        age = str(input("Digite a idade do jogador: "))
    return name, age


def check_age(player: str, age: str):
    if int(age) >= 18:
        print(f"{player}, you are an adult")
    elif 18 > int(age) >= 13:
        print(f"{player}, you are an adolecent")
    else:
        print(f"{player}, you are an child")


def main():
    players: dict = {}
    num: int = int(input("How many players? \n"))

    for i in range(num):
        players[i] = create_player()

    for k, v in players.items():
        check_age(players[k][0], players[k][1])


if __name__ == "__main__":
    main()
