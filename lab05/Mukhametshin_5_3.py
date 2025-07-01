lst = []
i = 1
while i < 11:
    lst.append(int(input(f'Enter the {i} number: ')))
    i += 1

mn = min(lst)
mx = max(lst)
mn_idx = lst.index(mn)
mx_idx = lst.index(mx)
print(lst)
lst[mn_idx] = mx
lst[mx_idx] = mn

print(lst)