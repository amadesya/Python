def factorial(n: 'Число для вычисления факториала'):
    """
    Рекурсивно вычисляет факториал числа n.
    Параметры:
    n (int): Число, для которого нужно вычислить факториал.
    Возвращает:
    int: Факториал числа n или -1 в случае ошибки.
    """
    if not isinstance(n, int) or n < 0:
        return -1 
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  
print(factorial(-3))  
print(factorial('a')) 
