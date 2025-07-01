l = input("Введите строку:\n").split()
c = {}
for el in l:
    if el not in c:
        c[el] = l.count(el)
for key in c.keys():
    print(c[key], end=' ')