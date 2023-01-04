a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if a >= b >= c:
    print (a, c)
elif a >= c >= b:
    print (a, b)
elif b >= a >= c:
    print (b, c)
elif c >= a >= b:
    print (c, b)
elif c >= b >= a:
    print (c, a)
else:
    print (b, a)
        
