class Store:
    def __init__(self, identificator: str, size: float = 0.0):
        self.id: str = identificator
        self.owner: str = ''
        self.size: float = size
        self.avalible: bool = False

    def rent(self):
        if (self.avalible is False) & (len(self.owner) < 1):
            self.owner = str(input('Who is the owner?\n'))
            self.avalible = True
            return 'Successuly rented!'
        else:
            return 'Rental its not avalible, please contact administrator!'

    def info(self):
        return self.__dict__

    def set_rent(self):
        pass
