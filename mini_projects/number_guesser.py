even = list(range(100))[::2]
odd = list(range(100))[1::2]
prime = [i for i in range(2, 100) if 0 not in [i % n for n in range(2, i)]]

def check(arg: str):
    return bool(answer.startswith('s'))

print("Pense em um numero de 0 a 100")
print("Seu numero é divisivel por 2?")
answer = str(input("Sim ou Não? ")).lower()
if check(answer):
    pass

# print("Seu numero é divisivel por 3?")