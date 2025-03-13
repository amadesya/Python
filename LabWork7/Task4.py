def multiply_elements(lst, multiplier=-1):
    return [x * multiplier for x in lst]


lst1 = [1, 2, 3, 4]
result1 = multiply_elements(lst1, 2)
print(result1)  # Ожидаемый вывод: [2, 4, 6, 8]

lst2 = [1, 2, 3, 4]
result2 = multiply_elements(lst2)
print(result2)  # Ожидаемый вывод: [-1, -2, -3, -4]
