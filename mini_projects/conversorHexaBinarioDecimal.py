
while True:
    typo = str(input("Insert the type of data you wish to convert(D/H/B/ 0 - exit): ")).lower()
    if typo == "0":
        print(" Thank you! ".center(50, "*"))
        break
    num = str(input("Insert the code you wish to convert: "))
    if typo == "d":
        print("Hexadecimal: ", hex(int(num)))
        print("Binary: ", bin(int(num)))

    elif typo == "h":
        print("Decimal: ", int(num, 16))
        print("Binary: ", bin(int(num, 16)))
    elif typo == "b":
        print("Hexadecimal: ", hex(int(num)))
        print("Decimal: ", int(num, 2))
    else:
        print("Please, inform a correct type of data")
        num = str(input("Insert the code you wish to convert: "))
