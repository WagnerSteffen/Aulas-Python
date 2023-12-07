solarSystem = {
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


def modifyDict(item):
    for key in item:
        print(key)
        for value in item[key]:
            print(value, item[key][value])
            newV = item[key][value] * 0.000001
            item[key][value] = newV
            print("New", item[key][value])
modifyDict(solarSystem)