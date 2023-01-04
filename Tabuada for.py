
começo = int(input('Começo = '))
fim = int(input('Fim = '))

for i in range(começo, fim+1):
    print('')
    for n in range(1,fim+1):
        print('%iX%i = %i'%(i, n, (i*n)))
