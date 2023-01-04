import random

dado_100 = []
n = int(input("Digite o número de lançamentos: "))
for i in range(n):
    dado_100.append(random.randint(1,6))
for i in range(6):
    print("O número %i foi achado %.2f%% vezes"%(i+1, 100*dado_100.count(i+1)/n))