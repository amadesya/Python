def statistics(*args: 'Числа для анализа'):
    """
    Выводит на экран сумму, среднее, максимум, минимум и количество всех чисел, переданных через параметры.
    Параметры:
    *args (int, float): Числа для анализа.
    Возвращает:
    None
    """
    if not args:
        return
    total = sum(args)
    count = len(args)
    average = total / count
    maximum = max(args)
    minimum = min(args)
    
    print(f"Сумма: {total}")
    print(f"Среднее: {average}")
    print(f"Максимум: {maximum}")
    print(f"Минимум: {minimum}")
    print(f"Количество: {count}")

statistics(1, 2, 3, 4, 5)
