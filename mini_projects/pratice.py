import copy


class Calculator:
    def __init__(self):
        self.result = 0
        self.value = 0
        self.equacion = []
        self.operations = ['sum', '+', 'sub', '-',
                           'mult', '*', 'div', '/',
                           'exp', '**', 'exp', '**',
                           'eq', '=']

    def display(self):
        if len(self.equacion) == 0:
            print('No Equacion')
        else:
            print("Equacion: [", *self.equacion, "]")
        print(f'{self.result}'.rjust())

    def getNumber(self):
        self.value = int(input("Insert your number: "))
        self.equacion.append(str(self.value))
        return self.value

    def getOperation(self):
        opr = str(
            input("What you wish to do(sum, sub, mult, div, exp, sqrt, eq)?  "))
        print(f'{opr}')
        while opr not in self.operations:
            print(self.operation)
            if opr in self.operations[:2]:
                opr = '+'
            elif opr in self.operations[2:4]:
                opr = '-'
            elif opr in self.operations[4:6]:
                opr = '*'
            elif opr in self.operations[6:8]:
                opr = '/'
            elif opr in self.operations[8:10]:
                opr = '**'
            elif opr in self.operations[10:12]:
                opr = '//'
            elif opr in self.operations[12:14]:
                opr = '='
                self.equacion.append(self.result)
            else:
                print("Unknown operation")
                opr = str(
                    input("What you wish to do(sum, sub, mult, div, exp, sqrt, eq)?  "))
        self.equacion.append(opr)
        return opr

    def reset(self):
        self.equacion = []

    def sum(self, value):
        self.result += value

    def sub(self, value):
        self.result -= value

    def div(self, value):
        self.result /= value

    def mult(self, value):
        self.result *= value

    def exp(self, exp):
        num = copy.copy(self.result)
        for _ in range(exp):
            self.result *= num

    def sqrt(self, exp):
        num = copy.copy(self.result)
        for _ in range(exp):
            self.result /= num


calc = Calculator()

keepCalc = True

while keepCalc:
    value = calc.getNumber()
    op = calc.getOperation()
    while op != '=':
        op = calc.getOperation()
        calc.display()
        calc.getNumber()
        calc.display()
        op = calc.getOperation()
        calc.display()
    keepCalc = bool(input("Wish to reset?"))
