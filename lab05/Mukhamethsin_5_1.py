i = 0
lst = []

while i < 10:
    lst.append(int(input()))
    i += 1

new_lst = [lst[i] for i in range(len(lst) - 1) if i % 2 == 0]
new_lst.sort(reverse=True)

print(new_lst)