import random

"""Matriz ordenada"""


def matrizOrd():
    matriz = []
    seq = list(range(16))
    for i in range(4):
        lista = []
        for j in range(4):
            num = seq[0]
            lista.append(num)
            seq.remove(num)
        matriz.append(lista)
    return print(matriz)


matrizOrd()

"""Matriz aleatória"""


def matrizAle():
    matriz = []
    seq = list(range(16))
    for i in range(4):
        lista = []
        for j in range(4):
            num = random.choice(seq)
            lista.append(num)
            seq.remove(num)
        matriz.append(lista)
    return print(matriz)


matrizAle()
