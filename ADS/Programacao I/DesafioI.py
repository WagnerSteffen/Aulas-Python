
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
                      'cnpj': int,
                      'rent': float}
        self.shopping_spaces: dict = {('E' + str(k)): store_hist for k, _ in zip(list(range(self.number_of_stores)), list(range(self.number_of_stores)))}
        return self.shopping_spaces

    def show_stores(self):
        """

        Returns:
            A string with the curruent places in the shopping, beeing avalible or not.

        """
        for store, _ in self.shopping_spaces.items():
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
        if len(store_info.dalayed_months) > 0:
            print("It's not possible to leave, there is a debt!")
            pay_now = input("Do you wish to pay the debt now? \n")
            if pay_now.startswith('y') | int(pay_now) == 1:
                self.pay_rent(store)
        else:
            self.shopping_spaces[store]['active'] = False
        return ' '

    def pay_rent(self, store: str) -> list:
        """
        Account a payment to the shopping from the store

        Args:
            store: Code of the store that is paying the rent

        Returns:
            A list with the months paid and another list with the debt, if there is one.
        """
        print("This are the month that you own: \n", self.shopping_spaces[store]['delayed_months'])

        confirmation = False

        while not confirmation:
            what_pay = input("Witch month are you going to pay? ")
            what_pay = what_pay.split(' ')
            difference = set(what_pay) - set(self.number_of_stores[store]['delayed_months'])

            if len(difference) > 0:
                print(f'There is some months that are not in debt: {" ".join(str(i) for i in difference)}')
            else:
                print(f"The selected months are: {what_pay}")
                confirmation = input("It's that correct? \n")

        return self.shopping_spaces[store]['delayed_months']






