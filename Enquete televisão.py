print("Enquete: Digite o número do melhor jogador da partida!")

lista_jogadores = []

num = int(input("Número do jogador (0=fim): "))

while num != 0:
    if num > 23:
        num = int(input("Número inválido. Digite um número entre 1 e 23: "))
    else:
        lista_jogadores.append(num)
        num = int(input("Número do jogador (0=fim): "))

print("")
votos = len(lista_jogadores)
print("Resultado da votação: ")
print("")
print("Foram compurados %i votos"%votos)

melhor_jogador = 0
for i in range(1,24):
    votos_jogador = lista_jogadores.count(i)
    if votos_jogador > 0:
        print("O jogador %i recebeu %i votos, totalizando %.2f%% do total"%(i, votos_jogador, 100*votos_jogador/votos))
        if votos_jogador > melhor_jogador:
            melhor_jogador = votos_jogador
            num_jogador = i
print("O melhor jogador foi o %i que recebeu %i votos, totalizando %.2f%% do total"%(num_jogador,lista_jogadores.count(num_jogador), 100*lista_jogadores.count(num_jogador)/votos))
