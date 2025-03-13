def hello(name: 'Имя пользователя' = None):
    """
    Функция выводит приветствие.
    Параметры:
    name (str): Имя пользователя. Если не передано, выводится "Hello, World".
    Возвращает:
    None
    """
    if name:
        print(f"Hello, {name}")
    else:
        print("Hello, World")


hello() 
hello("Иван")  
