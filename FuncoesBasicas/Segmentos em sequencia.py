n= int(input('Digite o tamanho da sequencia: '))
cont, ant, seq = 0, 0, 0
while cont < n:
    num = int(input('Digite o %i numero: '%(cont+1)))
    if num == ant:
        seq += 1
    ant = num
    cont += 1
print('A sequencia tem %i segmentos iguais'%(seq))
