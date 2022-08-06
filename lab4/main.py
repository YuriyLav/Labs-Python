import unittest

from Book import Book
from Magazine import Magazine
from Documentation import Documentation
from Textbook import Textbook
import unittest


# Пользовательское исключение NotNumber генерируется если введенное значение не число
class NotNumber(Exception):
    pass


# class Test(unittest.TestCase):
#     def test_average(self):
#         self.assertEqual(self.average_cost(), self.__cost/self.__count_str)


filename = "books"
assert len(filename) > 0, "Имя файла не может быть пустым"
mass = []
try:
    with open(filename, 'br') as f:
        file = f.readlines()
        for line in file:
            line = line.decode('utf-8')
            print("Объекты восстановленные из файла: ")
            print(line)
except IOError:
    print("Файл не найден! ")
    exit("Программа аварийно остановлена ")
book3 = Book()
print("\n" + "Инициализация с клавиатуры объекта типа Book")
name = input("Введите имя: ")
count_str = ""
cost = ""
try:
    count_str = input("Введите количество страниц: ")
    cost = input("Введите стоимость: ")
    if not count_str.isdigit() or not cost.isdigit():
        raise NotNumber("Введенное значение не является числом")
    count_str = int(count_str)
    cost = int(cost)
except ValueError:
    print("Преобразование прошло неудачно")
    exit("Программа аварийно остановлена ")
except NotNumber as e:
    print(e)
    exit("Программа аварийно остановлена ")
book3.set_name(name)
book3.set_count_str(count_str)
book3.set_cost(cost)
mass.append(Book(book3.get_name(), book3.get_count_str(), book3.get_cost()))
print("\n" + "Вывод новых объектов типа Book")
print(book3.print_object())
print("\n" + "Вывод средней стоимости одной страницы")
print(book3.average_cost())
# print(book3.Test.test_average())
# unittest.main
book4 = Magazine()
book5 = Documentation()
book6 = Textbook()
print("\n" + "Вывод объектов других типов")
print(book4.print_object())
print(book5.print_object())
print(book6.print_object())
with open(filename, 'ba') as f:
    assert len(mass) > 0, "Массив данных не может быть пустым"
    for line in mass:
        f.write(line.get_name().encode('utf-8') + " ".encode('utf-8') + str(line.get_count_str()).encode('utf-8')
                + " ".encode('utf-8') + str(line.get_cost()).encode('utf-8') + "\n".encode('utf-8'))
print()
