m = int(input("Digite o valor de m: "))

for i in range(1,m+1):
    primd = (i*(i-1))+1
    print('')
    print('%i*%i*%i = %i'%(i,i,i,(i**3)))
    print('+ %i'%(primd))
    for j in range(i-1):
        primd += 2
        print('+ %i'%(primd))
