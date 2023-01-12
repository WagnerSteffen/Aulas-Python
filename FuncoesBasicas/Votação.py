cand1, cand2, cand3 = (0, 0, 0)
eleitores = int(input('Digite o número de eleitores:'))

for votos in range(1, eleitores+1):
    voto = int(input('Eleitor %i digite em qual candidato deseja votar: '%(votos)))
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    else:
        print('Voto não computado')
por1 = (cand1*100)/eleitores
por2 = (cand2*100)/eleitores
por3 = (cand3*100)/eleitores
print('O candidato 1 recebeu %i votos, totalizando %i%% dos votos'%(cand1, por1))
print('O candidato 2 recebeu %i votos, totalizando %i%% dos votos'%(cand2, por2))
print('O candidato 3 recebeu %i votos, totalizando %i%% dos votos'%(cand3, por3))
