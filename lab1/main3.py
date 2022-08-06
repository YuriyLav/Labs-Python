st = input("Введите исходную строку ")
vir = input("Введите строку вирус ")
vir = vir.lower()
for i in range(0, len(st)-1):
    if st[i]+st[i + 1] == vir:
        s = st.replace(vir, "")
print(s)