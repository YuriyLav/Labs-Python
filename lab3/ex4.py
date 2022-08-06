res = []


def main():
    print("Введите промежуток от a до b (a<=b) ")
    a = int(input("a: "))
    b = int(input("b: "))
    if b < a:
        print("Введен неверный диапазон! ")
    else:
        simple_num(a, b)
        cort = tuple(res)
        print(cort)


def simple_num(a, b):
    for i in range(a, b+1):
        count = 0
        for j in range(1, b+1):
            if i % j == 0:
                count += 1
        if count == 2:
            res.append(i)


main()
