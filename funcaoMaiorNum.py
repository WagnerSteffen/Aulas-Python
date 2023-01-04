def sequencia(*nums):
    maior = nums[0]
    for num in nums:
        if num > maior:
            maior = num
    return maior


print(sequencia(1, 5, 4, 8, 77, 89, 5, 2, 4, 565, 45))
