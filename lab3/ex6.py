

def main():
    mas = intersect([1, 2, 3, 4, 5], [2, 4, 3, 10], [10, 2, 4])
    print(list(mas))


def intersect(*params):
    params = list(params)
    for i in range(len(params)):
        params[i] = set(params[i])
    list_set = params[0]
    for i in range(1, len(params)):
        list_set = list_set.intersection(params[i])
    return list_set


main()
