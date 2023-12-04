import random


class X1:
    def __init__(self, players: list):
        self.players = players

    def key(self):
        for player in self.players:
            self.players.remove(player)
            player2 = random.choice(self.players)
            print(player, " vs ", player2)


listOfPlayers = []
keepAdd = True
while keepAdd:
    p1 = str(input("Insert the name of the player (0 - exit): "))
    if p1 == "0":
        keepAdd = False
    else:
        listOfPlayers.append(p1)

championship = X1(listOfPlayers)
championship.key()
