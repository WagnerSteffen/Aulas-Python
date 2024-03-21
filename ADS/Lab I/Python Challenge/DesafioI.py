from Stores import Store


class Mall:

    def __init__(self):
        self.number_of_stores = None
        self.shopping_spaces: dict = {}

    def create_stores(self, number_of_stores: int) -> dict:
        self.number_of_stores = number_of_stores
        for store in range(self.number_of_stores):
            store_code = 'E'+str(len(self.shopping_spaces))
            self.shopping_spaces[store_code] = {'rented': False}
        print(self.shopping_spaces)

    def rent_store(self, store_code):
        if store_code in self.shopping_spaces.keys():
            store = Store(store_code)
            store.rent()
            self.shopping_spaces[store_code]['rented'] = True
            self.shopping_spaces[store_code]['object'] = store
            print(store.info())

    def info(self):
        return self.__dict__

    def load_json(self, data):
        self.shopping_spaces = data
