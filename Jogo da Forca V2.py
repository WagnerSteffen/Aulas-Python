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
    global blanc, palavra, wrong
    blanc = list()
    wrong = list()

    arquivo = abrir_arquivo()
    palavra = sortear_palavra(arquivo)
    """Caso programa esteja inserindo barra de espaço no final da palavra, adicionar função abaixo"""
    #palavra = corrige_palavra(palavra, " ")
    for letra in palavra:
        blanc.append("-")
    jogando = True
    while jogando:
        imprime_jogo(blanc, wrong)
        palpite = recebe_letra(blanc, wrong)
        redefine_blanc(palpite, palavra, )
        jogando = verifica_se_ganhou(blanc, wrong, palavra)


def abrir_arquivo():
    """
    Le arquivo com palavras que podem ser utilizadas
    como parte do jogo
    """
    with open("palavras.txt", "r") as arquivo:
        return arquivo.readlines()


def sortear_palavra(lista: str) -> list:
    """
    Retorna a palavra sorteada. Gera espaços em branco
    das letras ocultas.

    :param lista: palavras secretas
    :return: palavra sorteada 
    """

    return random.choice(lista).replace("\n", "").upper()


def imprime_com_espaço(algo: str):
    """ 
    Imprime "algo" com espaço entre as letras
    :param algo: palavra a ser espaçada

    """
    for letra in algo:
        print(letra, end=" ")
    print()


def imprime_jogo(
    letras_jogo: list,
    letras_erradas: list
):
    """ 
    Feito a partir da variável global que contem as imagens
    do jogo em ASCII art, e támbem as letras chutadas de
    maneira correta e as letras erradas e a palavra secreta

    :param letras_jogo: lista com letras em branco e acertadas
    :param letras_erradas: lista com letras erradas
    """
    global FORCAIMG
    print(FORCAIMG[len(letras_erradas)] + "\n")
    imprime_com_espaço(letras_jogo)
    print("\n")
    print("Letras erradas:", end=" ")
    imprime_com_espaço(letras_erradas)


def recebe_letra(
    a: list,
    b: list
):
    """
    Função que recebe palpite e garante que o palpite
    seja uma entrada válida.

    :param a:lista de letras manipulaveis
    :param b: lista de letras erradas
    :return: novo palpite
    """
    while True:
        palpite = input("Digite uma única letra: ").upper()
        if len(palpite) != 1:
            print("Coloque uma única letra.")
        elif palpite in a or palpite in b:
            print("Você já tentou essa letra. Escolha novamente")
        elif not "A" <= palpite <= "z":
            print("Digite somente letras.")
        else:
            return palpite


def verifica_se_ganhou(
    letras_jogo: list,
    letras_erradas: list,
    palavra_sorteada: str
) -> bool:
    """
    Verifia se ganhou ou perdeu.

    :param letras_jogo: lista de letras em jogo.
    :param letras_erradas: lista de letras erradas.
    :param palavra: palavra sorteada pelo jogo.
    :return: retorna bool para parar o jogo

    """
    if letras_jogo == list(palavra_sorteada):
        imprime_jogo(blanc, wrong)
        print("Ganhou!")
        venceu = False
    elif len(letras_erradas) == 6:
        imprime_jogo(blanc, wrong)
        print("Perdeu!")
        venceu = False
    else:
        venceu = True
    return venceu


def redefine_blanc(chute: str, palavra_sorteada: str, count=0):
    """
    Função que substitui os dashes pela letra caso coreto
    :param palpite: letra tentada pelo jogador
    :param palavra_sorteada: palavra sorteada
    :param count: parametro contador que por definição = 0
    """
    if chute not in palavra:
        wrong.append(chute)
    wordtext = []
    for letra in palavra_sorteada:
        wordtext += letra

    while chute in wordtext:
        blanc[(wordtext.index(chute))+count] = chute
        wordtext.remove(chute)
        count += 1


def corrige_palavra(palavra: str, caractere: str):
    """
    Função que elimina caracteres indesejados de uma string.

    :param palavra: string a ser corrigida
    :param caractere: caractere a ser removido.
    :return: retorna string ajustada ao novo formato.
    """
    lista_suporte = list()
    string_suporte = ""
    for i in palavra:
        lista_suporte.append(i)
    lista_suporte.remove(caractere)
    for j in lista_suporte:
        string_suporte += j
    return string_suporte


main()
