from Book import Book


class Documentation(Book):

    def set_type(self, type_doc):
        self.__type_doc = type_doc  # установка типа документации

    def get_type(self):
        return self.__type_doc

    def __init__(self, name="Documentation", count_str=50, cost=200, type_doc="Digital"):
        super().__init__(name, count_str, cost)  # Вызов конструктора родительского класса
        self.__type_doc = type_doc

    def print_object(self):  # перегрузка метода родителя
        s = Book.print_object(self) + "    " + "Тип документации: " + self.__type_doc
        return s
