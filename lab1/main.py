print("Введите ненулевые числа через enter, при вводе нуля программа остановится")
a = int(input())
sPol = 0
sOtr = 0
while a != 0:
    if a < 0:
        sOtr += a
    if a > 0:
        sPol += a
    a = int(input())
print("Сумма положительных чисел: "+str(sPol))
print("Сумма отрицательных чисел: "+str(sOtr))
