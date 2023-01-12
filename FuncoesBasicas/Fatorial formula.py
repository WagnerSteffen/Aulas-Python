n = int(input("Digite n: "))
x = float(input("Digite x: "))

cos = termo = 1

for i in range(1, n+1):
    termo *= (-(x**2)/(2*i*(2*i-1)))
    cos += termo

print("O cosseno de", x, "é", cos)
