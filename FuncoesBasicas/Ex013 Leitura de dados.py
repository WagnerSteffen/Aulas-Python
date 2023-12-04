usuarios = dict()

with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:
        usuario = linha[:15].strip()
        espaco = int(linha[15:].strip())
        usuarios[usuario] = espaco

espaco_total = sum(list(usuarios.values()))

print(
    """
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
"""
)

n = 1
for u, e in usuarios.items():
    output = f"{n}".ljust(5)
    output += f"{u}".ljust(15)
    ocup = ("%.2f" % (e / (1024**2))).rjust(8).replace(".", ",")
    ocup += " MB"
    output += ocup.ljust(21)

    output += ("%.2f%%" % (100 * e / espaco_total)).rjust(8).replace(".", ",")
    print(output)
    n += 1
