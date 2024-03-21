def get_cnpj(cnpj: str) -> int:
    """
    Recives a string and checks to see if it is a CNPJ valid
    Args:
        cnpj: The string to be tested

    Returns: Returns int with 14 numbers

    """
    only_digit: str = cnpj.replace('.', '').replace('/', '').replace("-", "")
    while not only_digit.isdigit() & (len(only_digit) == 14):
        if len(only_digit) != 14:
            print('CNPJ precisa ter 14 digitos')
        elif only_digit.isdigit() is False:
            print('Digite somente números')
        else:
            raise Exception('Erro desconhecido')
        only_digit: str = str(input('Digite o cnpj:\n').replace('.', '').replace('/', '').replace("-", ""))
    return int(only_digit)


def convert_months(numbers: list = None, names: list = None) -> list:
    """
    Takes a list of numbers and gives a list of names or other way around.
    Keyword Args:
        numbers: list of int with correspondent months
        names: List of str with correspondent 3 first letters from the month

    Returns: A list with correnpondent change

    """
    month_name_to_number = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    if numbers:
        list_of_names = [k for k, v in month_name_to_number.items() if v in numbers]
        return list_of_names
    if names:
        list_of_numbers = [v for k, v in month_name_to_number.items() if k in names]
        return list_of_numbers
