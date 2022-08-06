print("3-х значные и 4-х значные числа Армстронга: ")
for i in range(100, 9999):
    sum = 0
    count = 0
    var = i
    while var > 0:
        var = var // 10
        count += 1
    if count == 3:
        for s in range(0, 3):
            i = str(i)
            sum = sum + int(i[s]) ** 3
            i = int(i)
        if sum == i:
            print(i)
    if count == 4:
        for s in range(0, 4):
            i = str(i)
            sum = sum + int(i[s]) ** 4
            i = int(i)
        if sum == i:
            print(i)
