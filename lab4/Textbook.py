from Book import Book


class Textbook(Book):

    def set_type(self, grade):
        self.__grade = grade  # установка номера учебного класса

    def get_type(self):
        return self.__grade

    def __init__(self, name="Textbook mathematics", count_str=400, cost=500, grade=10):
        super().__init__(name, count_str, cost)  # Вызов конструктора родительского класса
        self.__grade = grade

    def print_object(self):  # перегрузка метода родителя
        s = Book.print_object(self) + "    " + "Номер учебного класса: " + str(self.__grade)
        return s
