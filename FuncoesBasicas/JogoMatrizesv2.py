import random
import sys

# Função princiapal


def main():
    venceu = False
    jogo = []
    geraMatriz(jogo)
    while not venceu:
        elezero = achaZero(jogo)
        ele1 = int(input("Digite o elemento 1 a ser trocado: "))
        lista = [-10, -1, 0, 1, 10]
        i = ele1 - elezero
        if i in lista:
            trocaElemento(ele1, elezero, jogo)
        else:
            print("Posição invalida.")
            dec = int(input("Deseja continuar jogando? 1 - SIM || 0 - NÃO: "))
            if dec == 0:
                sys.exit("Obrigado por jogar!")
        imprimeMatriz(jogo)


# gera o jogo


def geraMatriz(matriz):
    lista = list(range(16))
    for i in range(4):
        line = []
        for j in range(4):
            num = random.choice(lista)
            line.append(num)
            lista.remove(num)
        matriz.append(line)
    imprimeMatriz(matriz)
    return matriz


# Imprime a matriz


def imprimeMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

# Troca de elementos e verifica se venceu


def trocaElemento(ele1, ele2, matriz):
    global venceu
    elemento1 = matriz[ele1//10 - 1][ele1 % 10 - 1]
    elemento2 = matriz[ele2//10 - 1][ele2 % 10-1]
    matriz[ele1//10-1][ele1 % 10-1] = elemento2
    matriz[ele2//10-1][ele2 % 10-1] = elemento1

    # Verifica se venceu
    count = 0
    for i in range(4):
        for j in range(4):
            if (i*4 + j) == matriz[i][j]:
                count += 1
            else:
                break

    if count == 16:
        venceu = True
        print("Você venceu!")
    return matriz

# Acha o elemento zero


def achaZero(matriz):
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                zero = ((i+1)*10) + (j+1)
    return zero


main()
