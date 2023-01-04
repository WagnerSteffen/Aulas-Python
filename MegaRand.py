import random

jogo = []
sort = []
numeros = list(range(1,61))
mega_copy = numeros.copy()

for i in range(6):
    numsort = random.choice(mega_copy)
    jogo.append(numsort)
    mega_copy.remove(numsort)
print("Você recebeu o jogo: ", jogo)

mega_copy = numeros.copy()

for i in range(6):
    numsort = random.choice(mega_copy)
    sort.append(numsort)
    mega_copy.remove(numsort)
print("O jogo sorteado foi: ", sort)

if jogo == sort:
    print("Você ganhou!")
else:
    print("Você não ganhou  ='( ")
