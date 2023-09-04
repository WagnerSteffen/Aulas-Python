agenda = []

# construindo
while True:
    ordem = input("Deseja adicionar (add) ou parar (stop)? ").lower()
    if not ordem.isalpha():
        print("Digite apenas letras!")
    elif ordem.startswith("a"):
        entrada = {"Nome": input("Digite o nome da pessoa: ").capitalize()}
        entrada["Telefone"] = input("Digite o número de telefone: ")
        entrada["Endereço"] = input("Digite o endereço: ")
        entrada["Email"] = input("Digite o email: ")
        agenda.append(entrada)
    elif ordem.startswith("s"):
        break

print("A G E N D A \n")
for ent in agenda:
    print("Nome: ", ent["Nome"])
    print("Telefone: ", ent["Telefone"])
    print("Endereço: ", ent["Endereço"])
    print("Email: ", ent["Email"])
    print()
