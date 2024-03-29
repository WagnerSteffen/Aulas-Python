"""
Escreva um jogo de sobrevivência, no qual o player irá escolher entre
continuar, salvar e desistir.

CONTINUAR --> O jogo escolherá 1 entre 4 inimigos para lutar com o player,
SALVAR --> Salva o estado do player e o número de inimigos derrotados
DESISTIR --> Salva um arquivo de Score contendo o tanto de inimigos que o
player derrotou

O combate:
Cada personagem do jogo possuí os seguintes atributos:
Player --> For 20, Def 20, HP 500 e SP 100
Ogro --> For 30, Def 5, HP 100 e SP 5
Goblin --> For 15, Def 10, HP 70 e SP 10
Esqueleto --> For 20, Def 20, HP 80 e SP 20
Bruxo --> For 10, Def 30, HP 80 e SP 20

O jogador pode escolher entre os seguintes ataques:
Espadada, Flexada, Cura, Lança de Gelo

Já os inimigos
Ogro --> Clavada
Goblin --> Flexada
Esqueleto --> Espadada, Cura
Bruxo --> Relampago, Bola de Fogo, Espadada, Cura

A cada final de batalha o jogador pode escolher entre aumentar em 5 o valor
de um atributo ou recuperar todo HP ou recuperar todo SP

A cada 10 inimigos derrotados o número de inimigos em uma batalha dobra, e o
player os enfrenta SIMULTANEAMENTE

O calculo de dano é:
Espada --> max((For - Def)*random(0,1), 1) consumo de SP 0
Flexada --> max((For - Def/3)*random(0,1), 1) consumo de SP 2
Clavada --> max((For - Def/1)*random(0,1), 1) consumo de SP 0
Relampago --> max((For - Def/5)*random(0,1), 1) consumo de SP 5
BolaDeFogo --> max((For - Def/5)*random(0,1), 1) consumo de SP 10
LançaDeGelo --> max((For - Def/5)*random(0,1), 1) consumo de SP 10
Cura --> recupera 10 consumo de SP 10
"""
import dbm
import random
import datetime
import luta

class player():
    def __init__(self, name: str, strength=20, defense=20, hp=500, sp=100, attacks=None) -> None:
        if attacks is None:
            attacks = ['Espadada', 'Flexada', 'Cura', 'Lança de Gelo']
        self._name = name
        self._strength = strength
        self._defense = defense
        self._hp = hp
        self._sp = sp
        # self._save = datetime.datetime.now()
        self._enemiesDefeated = 0
        self.attacks = attacks
    def level_up(self, attribute):
        if attribute == 'strength':
            self._strenght += 5
        elif attribute == 'defense':    
            self._defense += 5
        elif attribute == 'hp':
            self._hp = 500
        elif attribute == 'sp':    
            self._sp = 100
        else:
            print("Attribute not supported")
def main():
    enemies_list = enemies()
    memory_card = dbm.open('saves.db', 'c')
    game = welcome_menu(memory_card)
    while game:
        enemies_in_wave = list(map(lambda wave: 1 if wave < 10 else wave // 10, [player._enemiesDefeated]))
        enemies_to_battle = [random.choice(enemies_list) for _ in enemies_in_wave[0]]

def welcome_menu(memory):
    print(
    """
    !WELCOME TO THE ADVENTURE GAME!
    """.center(60, " "))
    options = int(input(""" 
        1 - Continue
        2 - New Game
        3 - Saves
        0 - Exit
        """))
    if options == 0:
        return False
    elif options == 1:
        old_value = datetime.datetime(2020, 1, 1, 0, 0, 1, 000001)
        for value in memory.keys['save']:
            checkpoint = value if value > old_value else old_value 
        return checkpoint
    elif options == 2:
        name = str(input('What is the name of the character? \n'))
        new_player = player(name)
        
    elif options == 3:
        pass
    else:
        print('Only numbers, please!')
def player_menu():
    return int(
        input(
            """
    What you wish to do?
    1 - CONTINUE
    2 - SAVE
    3 - GIVE UP\n"""
        )
    )
def enemies():
    ogre = player("Ogre", 30, 5, 100, 5, ['Clavada'])
    goblin = player("Goblin", 15, 10, 70, 10, ['Flexada'])
    eskeleton = player("Eskeleton", 10, 20, 90, 20, ['Espadada', 'Cura'])
    witch = player("Witch", 10, 30, 80, 20, ['Relampago', 'Bola de Fogo', 'Espadada', 'Cura'])
    return [ogre, goblin, eskeleton, witch]

def enemies_in_wave(wave):
    return 1 if wave < 10 else wave // 10

def con():
    pass

def save():
    pass

def give_up():
    pass
if __name__ == '__main__':
    main()
    