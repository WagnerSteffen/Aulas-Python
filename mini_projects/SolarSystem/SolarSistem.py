class SolarSystem:
    def __init__(self):
        # Radius and distances of planets in meters
        self.solarSystem = {
            'mercury': {'radius': 2439.7 * 1e3, 'distanceToSun': 57909227.0 * 1e3},
            'venus': {'radius': 6051.8 * 1e3, 'distanceToSun': 108209475.0 * 1e3},
            'earth': {'radius': 6371.0 * 1e3, 'distanceToSun': 149597870.0 * 1e3},
            'mars': {'radius': 3389.5 * 1e3, 'distanceToSun': 227936637.0 * 1e3},
            'jupiter': {'radius': 69911.0 * 1e3, 'distanceToSun': 778412027.0 * 1e3},
            'saturn': {'radius': 58232.0 * 1e3, 'distanceToSun': 1426725400.0 * 1e3},
            'uranus': {'radius': 25362.0 * 1e3, 'distanceToSun': 2870972200.0 * 1e3},
            'neptune': {'radius': 24622.0 * 1e3, 'distanceToSun': 4498252900.0 * 1e3},
            'sun': {'radius': 696340.0 * 1e3, 'distanceToSun': 0.0}
        }


    def resizeSolarSystem(self, newSize):
        # newSize = float(input("Set the new radius of the sun in meters: "))
        Resize = self.solarSystem['sun']['radius'] / newSize
        def modifyDict(radius: float):
            print('Adjustin solar system...')
            for key in self.solarSystem:
                print(f'Adjusting {key.capitalize()}')
                for value in self.solarSystem[key]:
                    if value == 'radius':
                        self.solarSystem[key][value] = self.solarSystem[key][value] / radius
                    elif value == 'distanceToSun':
                        self.solarSystem[key][value] = self.solarSystem[key][value] / radius
                    else:
                        raise ValueError('Dicionario de dados não esta em conformidade')
        modifyDict(Resize)

    def show(self):
        for key in self.solarSystem:
            if self.solarSystem[key]["radius"] >= 1:
                print(f'\nThe new radius of {key} is {self.solarSystem[key]["radius"]:.5g} meters')
            else:
                print(f'\nThe new radius of {key} is {self.solarSystem[key]["radius"]*100:.5g} centimeters')
            print(f'The new distance to the Sun of {key} is {self.solarSystem[key]["distanceToSun"]:.2f} meters \n')

    def restart(self):
        self.solarSystem = {
            'mercury': {'radius': 2439.7 * 1e3, 'distanceToSun': 57909227.0 * 1e3},
            'venus': {'radius': 6051.8 * 1e3, 'distanceToSun': 108209475.0 * 1e3},
            'earth': {'radius': 6371.0 * 1e3, 'distanceToSun': 149597870.0 * 1e3},
            'mars': {'radius': 3389.5 * 1e3, 'distanceToSun': 227936637.0 * 1e3},
            'jupiter': {'radius': 69911.0 * 1e3, 'distanceToSun': 778412027.0 * 1e3},
            'saturn': {'radius': 58232.0 * 1e3, 'distanceToSun': 1426725400.0 * 1e3},
            'uranus': {'radius': 25362.0 * 1e3, 'distanceToSun': 2870972200.0 * 1e3},
            'neptune': {'radius': 24622.0 * 1e3, 'distanceToSun': 4498252900.0 * 1e3},
            'sun': {'radius': 696340.0 * 1e3, 'distanceToSun': 0.0}
        }
