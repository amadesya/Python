class Author:
    def __init__(self, full_name: str, country: str):
        """
        Инициализирует данные о авторе.
        :param full_name: Полное имя автора.
        :param country: Страна автора.
        """
        self.full_name = full_name
        self.country = country

    def display_info(self):
        """Метод, который выводит информацию об авторе."""
        print(f"Автор: {self.full_name}, Страна: {self.country}")

n = int(input("Введите количество авторов: "))
authors = []

for _ in range(n):
    full_name = input("Введите ФИО автора: ")
    country = input("Введите страну автора: ")
    author = Author(full_name, country)
    authors.append(author)

print("\nСписок всех авторов:")
for author in authors:
    author.display_info()

print("\nСписок русских авторов:")
for author in authors:
    if author.country.lower() == "россия":
        author.display_info()

class Book:
    def __init__(self, book_name: str):
        """
        Инициализирует книгу с заданным названием.
        :param book_name: Название книги.
        """
        self.book_name = book_name
        self.__content = []  
        print(f"Книга '{self.book_name}' создана.")

    def __del__(self):
        """Деструктор для вывода сообщения при удалении книги."""
        print(f"Книга '{self.book_name}' удалена.")

    #Task 3
    def add_work(self, work_name: str):
        """Метод для добавления произведения в содержание книги."""
        self.__content.append(work_name)

    #Task 3
    def get_work_count(self):
        """Метод, возвращающий количество произведений в книге."""
        return len(self.__content)
    
    #Task4
    def display_info(self):
        """Метод для вывода информации о книге и её содержании."""
        print(f"Книга: {self.book_name}")
        print("Содержание:")
        for i, work in enumerate(self.__content, 1):
            print(f"{i}) {work}")

book = Book("Моя книга")
book.add_work("Произведение 1")
book.add_work("Произведение 2")
book.display_info()
print(f"Количество произведений в книге: {book.get_work_count()}")
del book

class BookAuthor(Author, Book):
    def __init__(self, full_name: str, country: str, book_name: str):
        """
        Инициализирует книгу с автором и её названием.
        :param full_name: ФИО автора.
        :param country: Страна автора.
        :param book_name: Название книги.
        """
        Author.__init__(self, full_name, country) 
        Book.__init__(self, book_name)  

    def display_full_info(self):
        """Выводит ФИО автора, название книги и содержание книги."""
        self.display_info()
        print(f"Автор: {self.full_name}")
        print(f"Страна: {self.country}")

book_author = BookAuthor("Достоевский Ф.М.", "Россия", "Преступление и наказание")
book_author.add_work("Часть 1")
book_author.add_work("Часть 2")
book_author.display_full_info()
