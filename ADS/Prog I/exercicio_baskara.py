
# x = -b*((b**2) - (4*a*c))**(1/2)

# ax**2 + bx + c = 0
def baskara(a: int, b: int, c: int) -> list:
    x1 = (-b + ((b ** 2) - (4 * a * c)) ** (1 / 2)) / (2 * a)
    x2 = (-b - ((b ** 2) - (4 * a * c)) ** (1 / 2)) / (2 * a)
    return [x1, x2]


def main():
    while True:
        print("Ax^2 + Bx + C = 0")
        a, b, c = [int(i) for i in input("Digite os valores de A, B e C: ").split(" ")]
        confirm: str = input(f"A formula é: {a}x^2 + {b}x + {c} = 0 ?\n")
        if confirm.startswith('s') | (confirm == '1'):
            result = baskara(a, b, c)
            print(f'Os resultados são: \nX1 = {result[0]}\nX2 = {result[1]}')
            cont = input("Deseja inserir mais uma formula?\n")
            if cont.startswith('s') | (cont == '1'):
                continue
            else:
                print('Obrigado por participar!')
                break


if __name__ == "__main__":
    main()
