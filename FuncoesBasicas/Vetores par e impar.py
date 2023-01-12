lista_par = []
lista_impar = []

for i in range(20):
    vector = int(input("Digite o %i número: "%(i+1)))
    if vector%2 == 0:
        lista_par.append(vector)
    else:
        lista_impar.append(vector)
print(lista_par)
print(lista_impar)
