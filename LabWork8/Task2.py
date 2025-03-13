def decimal_to_base(n: 'Число', base: 'Основание системы счисления'):
    """
    Рекурсивная функция для перевода числа из десятичной системы счисления в N-ричную.
    Параметры:
    n (int): Число, которое нужно перевести.
    base (int): Основание системы счисления.
    Возвращает:
    str: Число в N-ричной системе.
    """
    if n == 0:
        return ''
    else:
        return decimal_to_base(n // base, base) + str(n % base)

print(decimal_to_base(255, 2)) 
print(decimal_to_base(255, 16))  
