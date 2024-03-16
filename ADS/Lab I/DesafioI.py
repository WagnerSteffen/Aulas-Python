from datetime import datetime, date
import FuncoesSecundarias as fs


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
        store_hist: dict = {'active': False,
                            'payed_months': [],
                            'to_pay_months': [],
                            'type_store': [],
                            'start_date': '',
                            'end_date': '',
                            'owner': '',
                            'cnpj': 0,
                            'rent': 0.0}
        self.shopping_spaces: dict = {('E' + str(k)): store_hist for k, _ in
                                      zip(list(range(self.number_of_stores)), list(range(self.number_of_stores)))}
        return self.shopping_spaces

    def show_stores(self, store: str = None) -> None:
        """
            Recives a string with the code of the store and prints it infos. If no code given, print
            all information about all stores.
        Returns:
            A string with the curruent places in the shopping, beeing avalible or not.

        """
        if not store:
            for store, _ in self.shopping_spaces.items():
                print(f'Store: {store}')
                for k, v in self.shopping_spaces[store].items():
                    print(f'{k}: {v}')
                print('\n')
        else:
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
        if self.shopping_spaces[store]['active'] is False:
            # Fazer copia para nao alterar todas as chaves
            to_rent = self.shopping_spaces[store].copy()
            print("\nPrecisamos de algumas informações antes de locarmos o espaço\n")
            today: str = str(datetime.now().date())
            owner: str = str(input('Digite o nome completo do locatario:\n'))
            cnpj: str = str(input('Digite o cnpj do locatario:\n'))
            cnpj: int = fs.get_cnpj(cnpj)
            to_rent['start_date'] = today
            to_rent['owner'] = owner
            to_rent['cnpj'] = cnpj
            to_rent['to_pay_months'] = [int(datetime.now().date().month)]
            to_rent['active'] = True
            # Reatribuir a chave em questao para validacao
            self.shopping_spaces[store] = to_rent
            print('\nLoja locada com sucesso!\n')
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
        store_info = self.shopping_spaces[store].copy()
        if len(store_info['to_pay_months']) > 0:
            print("It's not possible to leave, there is a debt!")
            pay_now = input("Do you wish to pay the debt now? \n")
            if pay_now.startswith('y') | int(pay_now) == 1:
                self.pay_rent(store)
        else:
            store_info['active'] = False
        return ' '

    def pay_rent(self, store: str) -> list:
        """
        Account a payment to the shopping from the store

        Args:
            store: Code of the store that is paying the rent

        Returns:
            A list with the months paid and another list with the debt, if there is one.
        """
        store_info = self.shopping_spaces[store].copy()
        print("This are the month that you own: \n", store_info['to_pay_months'])

        confirmation = False

        while not confirmation:
            what_pay: str = str(input("Witch month are you going to pay? "))
            what_pay: list = what_pay.split(' ')
            what_pay: list = [int(i) for i in what_pay]
            difference: list = [month for month in what_pay if month not in store_info['to_pay_months']]

            if len(difference) > 0:
                print(f'There is some months that are not in debt: {" ".join(str(i) for i in difference)}')
            else:
                print(f"The selected months are: {what_pay}")
                confirm: str = str(input("It's that correct? \n"))
                if confirm.startswith('s') | (confirm == '1'):
                    store_info['to_pay_months'] = [month for month in store_info['to_pay_months']
                                                   if month not in what_pay]
                    break

        self.shopping_spaces[store] = store_info
        return self.shopping_spaces[store]

    def __json__(self):
        return self.shopping_spaces

    def load_json(self, data):
        self.shopping_spaces = data
