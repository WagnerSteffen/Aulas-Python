import random
print("Hello, this is a game of Rock, Paper and Cisors!")
options = ("Rock", "Paper", "Cisors")

def main():
    #show game
    while True:
        c_choice = computer_choice()
        p_choice = player_choice()
        print(f"\nYou choose {p_choice} and the computer choose {c_choice}\n")
        who_wins = determine_winner(p_choice, c_choice)
        keep_playing = str(input("\nDo you wanna play again?\n")).lower()
        if not keep_playing.startswith("y"):
            break
def player_choice():
    print("\n")
    for num, op, in enumerate(options):
        print(num, op)
    p_choice = int(input("What do you chose? \n:"))
    print("\n")
    return options[p_choice]
def computer_choice(y = options):
    return random.choice(y)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return print("It's a tie!")

    if player_choice == "Rock":
        if computer_choice == "Paper":
            return print("Computer wins")
        else:
            return print("You win!")

    if player_choice == "Paper":
        if computer_choice == "Cisors":
            return print("Computer wins")
        else:
            return print("You win!")

    if player_choice == "Cisors":
        if computer_choice == "Rock":
            return print("Computer wins")
        else:
            return print("You win!")

main()
print(f"You win {count} times")