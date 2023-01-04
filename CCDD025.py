h = float(input("Digite a sua altura: "))
hm = int(input("Digite 0 para homem e 1 para mulher: "))

if hm == 0:
    x = (72.7*h)-58
    p = float(input("Digite seu peso: "))
    if x > p:
        print("Você está abaixo do peso. Seu peso ideal é %.2fkg"%x)
    elif x == p:
        print("Você está no peso ideal")
    else:
        print("Você está acima do peso. Seu peso ideal é %.2fkg"%x)
elif hm == 1:
    x = (61.1*h)-44.7
    p = float(input("Digite seu peso: "))
    if x > p:
        print("Você está abaixo do peso. Seu peso ideal é %.2fkg"%x)
    elif x == p:
        print("Você está no peso ideal")
    else:
        print("Você está acima do peso. Seu peso ideal é %.2fkg"%x)
else:
    print("Entrada inválida")

