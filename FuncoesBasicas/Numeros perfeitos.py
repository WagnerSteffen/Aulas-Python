n = int(input("Digite n: "))
cont, soma = 2, 1
while cont < n:
    if n % cont == 0:
        soma += cont
    cont += 1
if soma == n:
    print ("O número", n, "é perfeito")
else:
    print ("O número", n, "não é perfeito")
