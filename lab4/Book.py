class Book:

    def __init__(self, name="Book", count_str=100, cost=500):
        self.__name = name  # установка имени книги
        self.__count_str = count_str  # установка количества страниц книги
        self.__cost = cost  # установка стоимости книги

    def __del__(self):
        print("Объект " + self.__name + " удален из памяти")

    def set_name(self, name):
        self.__name = name

    def set_count_str(self, count_str):
        self.__count_str = count_str

    def set_cost(self, cost):
        self.__cost = cost

    def get_name(self):
        return self.__name

    def get_count_str(self):
        return self.__count_str

    def get_cost(self):
        return self.__cost

    def average_cost(self):
        var1 = self.__cost
        var2 = self.__count_str
        return "Средняя стоимость одной страницы: " + str(var1 / var2)

    def increase_cost(self):
        self.__cost *= 2

    def print_object(self):
        s = "Название: " + self.__name + "    " + "Стоимость 1 страницы: " + str(self.__count_str) + "     " \
            + "Стоимость: " + str(self.__cost)
        return s

    # def virtual print_name_upper(self):
    # return self.__name.upper
