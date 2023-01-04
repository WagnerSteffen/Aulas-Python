
#Calcula o numero de digitos de p
aux_p = p
cont_d = 0
while aux_p != 0:
    aux_p //= 10
    cont_d+=1


#Comparação
#p é sub de q --> paro execução
#q == 0
comparando = True
aux_q = q
while comparando:
    subnum = aux_q%(10**cont_d)
    if subnum == p:
        comparando = False

    aux_q //= 10

    if aux_q == 0:
        comparando = False

if subnum == p:
    print("%i é subnumero de %i" %(p, q))
else:
    print("%i não é subnumero de %i" %(p, q))
