import SolarSistem

while True:
    opening = str(input("Do you wish to resize the Solar System? ")).lower()
    if opening.startswith('y'):
        solars = SolarSistem.SolarSystem()
        solars.restart()
        size = float(input('Wich size the Sun should be in this model? '))
        solars.resizeSolarSystem(size)
        solars.show()
        continue
    elif opening.startswith('n'):
        print('See you soon!')
        break
    else:
        raise ValueError('Entrada inválida!')