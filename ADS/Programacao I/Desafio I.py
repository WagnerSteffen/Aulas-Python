
class Mall:

    def __init__(self, number_of_stores: int):
        """
        Create a mall with the given number of slots for new stores

        Args:
            number_of_stores: The number of slots avalible to be rented
        """
        self.number_of_stores = number_of_stores
        self.shopping_spaces: dict = {}

    def create_stores(self) -> dict:
        """
        Takes the amout of stores that was given when creating the class and
        create a dictionary with information to every slot avalible

        Returns:
            A dict with every store avalible in the mall
        """
        store_hist = {'active': bool,
                      'payed_months': int,
                      'delayed_months': int,
                      'type_store': str,
                      'start_date': str,
                      'end_date': str,
                      'owner': str,
                      'cnpj': int}
        self.shopping_spaces: dict = {('E' + str(k)): store_hist for k, _ in zip(list(range(self.number_of_stores)), list(range(self.number_of_stores)))}
        return self.shopping_spaces

    def show_stores(self):
        """

        Returns:
            A string with the curruent places in the shopping, beeing avalible or not.

        """
        for store,_ in self.shopping_spaces.items():
            print(f'Store: {store}')
            for k, v in self.shopping_spaces[store].items():
                print(f'{k}: {v}')
            print('\n')

    def rent_store(self, store: str) -> str:
        """
        Checks to see if you can rent a space in the shopping, if yes, it
        locks the place with the new owner

        Args:
            store: The correspondent code of the store. Ex: 'E12'

        Returns:
            String with information about the code resolution

        """
        if not self.shopping_spaces[store]['active']:
            self.shopping_spaces[store]['active'] = True
            print('Loja locada com sucesso!')
        else:
            print(f'A loja {store} não está disponível para locação')

        return ' '

    def leave_shopping(self, store: str) -> str:
        """
        Close a store in the shopping, if no debt in the rent

        Args:
            store: The code of the store that it suppost to be closed

        Returns:
            String with information about the code resolution.

        """
        store_info = self.shopping_spaces[store]

        return ' '

    def pay_rent(self, store: str, month: str) -> list:
        """
        Account a payment to the shopping from the store

        Args:
            store: Code of the store that is paying the rent
            month: Numeber of the moth that's beeing paid

        Returns:
            A list with the months paid and another list with the debt, if there is one.
        """
        pass


def menu() -> input:
        """
        Show a menu to navegate between options

        Returns:
            Input of options

        """


if __name__ == '__main__':
    menu()
