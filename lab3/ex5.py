res = [1000, 900, 500, 3, 2, 1]


def main():
    print(monotone(res))


def monotone(seq):
    count = 0
    count1 = 0
    for i in range(0, len(seq)-1):
        if seq[i] < seq[i+1]:
            count += 1
        if seq[i] > seq[i+1]:
            count1 += 1
    if count == len(res) - 1:
        return True
    elif count1 == len(res) - 1:
        return True
    else:
        return False


main()
