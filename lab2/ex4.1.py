with open("inputEx5.txt", "r", encoding='utf-8') as file:
    str1 = file.read()
    str1 = str1.replace(" ", "")
    freq = {}
    for i in str1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(str(freq))
