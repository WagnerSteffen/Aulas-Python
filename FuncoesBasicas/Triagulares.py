
num = int(input("Digite um número: "))
k=1
n=0
while k * (k+1) * (k+2) < num:
    k += 1
    n = k*i*j
if n == num:
    print(num, "é triangular")
else:
    print(num, "não é triangular")
