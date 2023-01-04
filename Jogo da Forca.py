import random


FORCAIMG = [
    """

      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""",
    """

      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========""",
]


def main():
    global guess, countForca, wordtext, keepG
    keepG = True
    countForca = 0  # variavel de contagem de erros
    guess = []  # lista com as letras erradas

    sorteio()
    wordtext = ""
    imprime_jogo()
    while keepG == True:
        tent = str(input("Digite a letra: "))
        for w in palavra:
            wordtext += w
        alpha_try(tent, )
        imprime_jogo()
        keepG = verifica_se_ganhou()
    if definicao == 0:
        print("Ah, que pena, mas você pode tentar de novo.")
    if definicao == 1:
        print("Parabéns! Você ganhou.")


def verifica_se_ganhou():
    global definicao, keepG
    if countForca > 6:
        keepG = False
        definicao = 0
    elif write_ == palavra:
        keepG = False
        definicao = 1
    else:
        keepG = True
    return keepG


def imprime_jogo():
    global word, write_
    write_ = ""
    for item in word:
        write_ += item
    output = f"{FORCAIMG[countForca]}".ljust(10)
    output += (" "*3)
    output += f"{write_}".rjust(15)
    print(output)
    print("Letras tentadas: ", guess)


def sorteio():
    with open("palavras.txt", "r") as arquivo:
        global palavra, word
        palavras = dict()
        for linha in arquivo:
            chave = linha[:15].strip()
            palavras[chave] = "-"
        lista = list(palavras.keys())
        palavra = str(random.choice(lista))
        word = []
        for i in palavra:
            word.append("- ")


def alpha_try(a1: str, a2=0):
    global countForca
    while a1 in guess:
        print("Você já tentou essa letra.")
        a1 = str(input("Digite outra letra: "))
    if a1 not in palavra:
        countForca += 1
    guess.append(a1)

    wordtext = []
    for letra in palavra:
        wordtext += letra

    while a1 in wordtext:
        word[(wordtext.index(a1))+a2] = a1
        wordtext.remove(a1)
        a2 += 1

    return a1


main()
jogar = input("Deseja jogar de novo? ")
if "s" in jogar or "y" in jogar:
    main()
else:
    print("Obrigado por jogar!")
