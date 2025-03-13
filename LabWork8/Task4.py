def caesar_cipher(text: 'Текст для шифрования', shift: 'Количество сдвигов' = 3):
    """
    Функция для шифрования текста с использованием шифра Цезаря.
    Параметры:
    text (str): Текст, который нужно зашифровать.
    shift (int): Сдвиг алфавита для шифра. По умолчанию равен 3.
    Возвращает:
    str: Зашифрованный текст.
    """
    result = []
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result.append(chr((ord(char) - offset + shift) % 26 + offset))
        else:
            result.append(char)
    return ''.join(result)

print(caesar_cipher("Hello, World!"))  
print(caesar_cipher("Hello, World!", 5))
