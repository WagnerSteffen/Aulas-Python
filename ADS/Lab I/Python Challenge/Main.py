from DesafioI import Mall



def main():
    shopping1 = Mall()
    shopping1.create_stores(20)
    shopping1.rent_store('E1')
    print(shopping1.info())
    print(shopping1['E1'])


    mall = DesafioI.Mall(20)
    mall.create_stores()
    while True:
        menu = """
        MENU PRINCIPAL
        1 - Acessar Loja
        2 - Mostrar lojas
        3 - Salvar dados
        4 - Carregar dados
        0 - Sair
        """
        submenu_loja = """
        LOJA: {}
        1 - Alugar loja
        2 - Pagar aluguel
        3 - Visualizar informações
        4 - Fechar loja
        0 - Retornar ao menu principal
        """
        print("O que deseja fazer?")
        print(menu)
        op = int(input('Digite o número da opçáo desejada: '))
        if op == 1:
            loja = str(input("Qual o código da loja que deseja acessar? \n")).upper()
            while True:
                print(submenu_loja.format(loja))
                sub_op = int(input('\nDigite o número da opçáo desejada: '))
                if sub_op == 1:
                    mall.rent_store(loja)
                elif sub_op == 2:
                    mall.pay_rent(loja)
                elif sub_op == 3:
                    mall.show_stores(loja)
                elif sub_op == 4:
                    mall.leave_shopping(loja)
                elif sub_op == 0:
                    break
                else:
                    raise Exception('Opção indisponível!')
        elif op == 2:
            loja = str(input("Qual o código da loja que deseja visualizar? (0 - Todas)\n")).upper()
            if loja == '0':
                mall.show_stores()
            else:
                mall.show_stores(loja)
        elif op == 3:
            file_path = 'data.json'
            with open(file_path, 'w') as json_file:
                json.dump(mall.__json__(), json_file, indent=4)

            print("\nJSON file created successfully.\n")
        elif op == 4:
            file_path = 'data.json'
            with open(file_path, 'r') as json_file:
                json_data = json.load(json_file)
            mall.load_json(json_data)

        elif op == 0:
            print("Até breve!")
            break
        else:
            raise Exception('Opção indisponível!')


if __name__ == '__main__':
    main()
