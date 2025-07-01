d = {"1": 1, "4": 4, "five": 5, "zero": 0, "7": 7}

val = int(input("Введите значение: "))
f = False
for key in d:
    if d.get(key) == val:
        print(key)
        f = True
if not f:
    print("значение отсутствует")