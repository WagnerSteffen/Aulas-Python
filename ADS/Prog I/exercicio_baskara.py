def baskara(a: int, b: int, c: int) -> list:
    """
    Calcula a formula de baskara para uma dada funcao de segundo grau
    Args:
        a: primeiro termo da funcao de segundo grau
        b: Segundo termo da funcao de segundo grau
        c: Terceiro Termo da funcao de segundo grau

    Returns: valores de X1 e X2 em uma lista

    """
    x1 = (-b + ((b ** 2) - (4 * a * c)) ** (1 / 2)) / (2 * a)
    x2 = (-b - ((b ** 2) - (4 * a * c)) ** (1 / 2)) / (2 * a)
    return [x1, x2]


def main():
    while True:
        print("Ax^2 + Bx + C = 0")
        while True:
            termos = input("Digite os valores de A, B e C: ").replace(',', '').split(" ")
            if (len(termos) == 3) & ("".join(termos).isdigit()):
                break
            elif len(termos) > 3:
                print(f'\nVoce digitou {len(termos)} termos, digite apenas 3 termos\n')
            elif len(termos) < 3:
                print(f'\nVoce digitou {len(termos)} termos, digite 3 termos\n')
            else:
                print(f'\nDigite apenas números\n')
        a, b, c = [int(i) for i in termos]
        confirm: str = input(f"A formula é: {a}x^2 + {b}x + {c} = 0 ?\n")
        if confirm.startswith('s') | (confirm == '1'):
            result = baskara(a, b, c)
            print(f'Os resultados são: \nX1 = {result[0]:.2f}\nX2 = {result[1]:.2f}')
            cont = input("Deseja inserir mais uma formula?\n")
            if cont.startswith('s') | (cont == '1'):
                continue
            else:
                print('Obrigado por participar!')
                break


if __name__ == "__main__":
    main()
