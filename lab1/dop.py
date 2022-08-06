count = int(input("Введите величину магического числа "))
digit = 19
i = 0
s = 0
flag = True
while flag:
    x = digit
    while x > 0:
        s += x % 10
        x = x // 10
    if s == 10:
        i += 1
    if i == count:
        print(digit)
        break
    digit += 1
    s = 0
