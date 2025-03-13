import re

def print_sentences(text: 'Текст'):
    """
    Функция принимает текст и выводит каждое предложение с новой строки.
    Параметры:
    text (str): Текст, состоящий из предложений.
    Возвращает:
    None
    """
    sentences = re.split(r'(?<=\.)\s*', text)
    for sentence in sentences:
        print(sentence)

print_sentences("Madoka Kaname (鹿目まどか?) is one of the five main Magical Girls and the title character of Puella Magi Madoka☆Magica anime and manga series."
" She's a second-year student at Mitakihara Middle School and is in the same class as Sayaka and Homura."
" In Episode 12, she transformed into a goddess known as Ultimate Madoka (アルティメットまどか?).")
