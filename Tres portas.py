import random
c = int(input("Digite o número da porta que deseja escolher: "))
escolha = random.randint(1,3)  

#escolhendo a porta com bode
if c and escolha != 2:
     rdoor = 2
elif c and escolha != 3:
     rdoor = 3
else:
     rdoor = 1

print("Você escolheu aporta número %i /n Na porta número %i há um bode."%(c,rdoor))
#deseja trocar?
troca = int(input("Deseja trocar de porta? 1-SIM  2-NÃO: "))
if troca == 1:
     if c != 1 and rdoor != 1:
          c2 = 1
     elif c != 2 and rdoor != 2:
          c2 = 2
     else:
          c2 = 3
       
if c == escolha:
    print("Ganhou um carro!")
else:
    print("Não ganhou um carro...")

