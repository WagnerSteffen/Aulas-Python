num = int(input("Digite o numero de temperaturas registradas: "))
soma = maior = menor = float(input('Digite a 1 temperatura: '))

for i in range(2, num+1):
    temp = float(input("Digite a %d temperatura: "%i))
    soma += temp

    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp
media = (soma/num)
print("A maior temperatura é: %.2f"%maior)
print("A menor temperatura é: %.2f"%menor)
print("A média das temperaturas é: %.2f"%media)
