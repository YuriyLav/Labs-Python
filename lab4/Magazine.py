from Book import Book


class Magazine(Book):

    def set_author(self, author):
        self.__author = author  # установка имени автора

    def get_author(self):
        return self.__author

    def __init__(self, name="Magazine", count_str=400, cost=600, author="Unknown"):
        super().__init__(name, count_str, cost)  # Вызов конструктора родительского класса
        self.__author = author

    def print_object(self):  # перегрузка метода родителя
        s = Book.print_object(self) + "    " + "Имя автора: " + self.__author
        return s