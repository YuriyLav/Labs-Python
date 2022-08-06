pascal = []


def main():
    n = int(input("Введите число строк треугольника Паскаля "))
    for i in range(0, n):
        pascal.append(next_line(i))
    for p in pascal:
        print(p)


def next_line(k):
    row = [1] * (k + 1)
    for j in range(0, k+1):
        if j != 0 and j != k:
            row[j] = pascal[k - 1][j - 1] + pascal[k - 1][j]
    return row


main()
