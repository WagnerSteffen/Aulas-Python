n = 1000
while n < 10000:
    pdez = (n//100)
    sdez = (n%100)
    soma = pdez+sdez
    quadrado = soma**2

    if quadrado == n:
        print(n)
    n += 1
