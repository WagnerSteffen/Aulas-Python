n = int(input("Digite o valor de n: "))
div = 0
for i in range(1, n+1):
    primo = True
    j = 2
    if j< i and primo:
        div +=1
        if i%j == 0:
            primo  = False
        j += 1
    if primo:
        print(i)
print('%i divisões'%div)
