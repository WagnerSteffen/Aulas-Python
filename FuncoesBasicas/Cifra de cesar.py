#dict(zip(list("abc"), (1, 2, 3)))
"""Cifra de César"""

# Decisão C or D
from calendar import c


while True:
    dec = str(input("Você deseja criptografar(C) ou descriptografar(D)? ")).lower()
    if dec in ["c", "d"]:
        break
    else:
        print("Utilize 'c' ou 'd'")

# Mensagem
mensagem = input("Digite a mensagem: ").lower()

# Lidando com caracteres especiais
orig = "áàãâéèêíìîóòõôúùûç"
sub = "aaaaeeeiiioooouuuc"
repl = dict(zip(orig, sub))
for o, r in repl.items():
    mensagem = mensagem.replace(o, r)

# Determinando a chave
while True:
    chave = int(input("Digite a chave (1-26): "))
    if 1 <= chave <= 26:
        break
    else:
        print("Digite um número entre 1 e 26")

# Se descriptografar
if dec == "d":
    chave *= -1

# alocação da mensagem final
translate = ""
# Codding Cripto
for caractere in mensagem:
    if caractere.isalpha():
        num = ord(caractere)

        num += chave

        if num > ord("z"):
            num -= 26
        if num < ord("a"):
            num += 26
        translate += chr(num)

    else:
        translate += caractere

print(translate)
