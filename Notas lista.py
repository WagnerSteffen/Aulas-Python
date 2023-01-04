notas = []
soma = 0

for i in range(1,5):
    nota = float(input("Digite a %i nota: "%i))
    notas.append(nota)
    soma += nota

for i in range(4):
    print("A nota %i foi: %i"%(i+1, notas[i]))
print("A média foi: %.1f"%(soma/4))
