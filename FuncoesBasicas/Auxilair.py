palavra = list("abelha")
word = list("_"*(len(palavra)))
count = 0
palavra2 = palavra.copy()

letra = str(input("Digite uma letra: "))
while letra in palavra2:
    word[(palavra2.index(letra)+count)] = letra
    palavra2.remove(letra)
    count += 1
