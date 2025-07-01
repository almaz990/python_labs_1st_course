lst = [1, 2, 3, 4, 5, 6]


def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 != 0:
            l.remove(l[i])
        else:
            l[i] //= 2
            i += 1


print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)