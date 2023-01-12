import random
portas = list(range(1, 4))

print("\nBem vindo! Escolha uma das portas para começar o jogo!\n")

# Set porta premiada e escolha do jogador
premio = random.choice(portas)
escolha = int(input("Deseja escolher a porta 1, 2 ou 3? "))

# abrindo porta com bode
for i in portas:
    if escolha != i != premio:
        print("A porta %i tem um bode" % i)
        portas.remove(i)

# Troca de portas
nova_escolha = input("Deseja trocar de porta?(y/n): ").lower()
if nova_escolha in ["y"]:
    portas2 = portas
    portas2.remove(escolha)
    escolha = portas2[0]  # tornando a lista um inteiro
elif nova_escolha in ["n"]:
    print("Você manteve a porta %i" % (escolha))

# resultado final
if premio == escolha:
    print("Parabéns! Você ganhou o premio!!")
elif premio != escolha:
    print("Que pena, o premio estava na porta %i" % (premio))
else:
    print("Erro!")
