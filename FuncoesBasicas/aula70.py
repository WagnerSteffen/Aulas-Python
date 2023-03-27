while True:
    try:
        num = int(input("Digite um numero entre 1 e 20: "))
    except ValueError:
        print("Digite apenas numeros")
    except Exception:
        print("Entrada invalida")
    else:
        break

test = 1 <= num <= 20
assert test, num

if __debug__ and not test:
    raise AssertionError(num)