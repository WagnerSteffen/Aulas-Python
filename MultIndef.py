def mult(*nums):
    mult_nums = 1
    for n in nums:
        mult_nums *= n
    return mult_nums


print(mult(2, 5, 7, 8, 9))
