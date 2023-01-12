n = int(input("Digite n: "))

cont, soma = 0, 0

while cont < n:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
    cont += 1
print(soma)
