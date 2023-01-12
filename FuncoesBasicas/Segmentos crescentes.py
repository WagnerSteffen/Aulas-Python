n = int(input('Digite o tamanho da sequencia n: '))
cont, aux, soma, seqMAX = 0, 0, 0, 1

while cont < n:
    num = int(input('Digite o %i número: '%(cont+1)))
    if num > aux:
        soma += 1
        aux = num
    else:
        seqMAX = 1
        aux = num
    if soma > seqMAX:
        seqMAX = soma
    cont += 1
print('O comprimento do segmento crescente máximo é %i'%(seqMAX))
