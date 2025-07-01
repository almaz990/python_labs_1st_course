lst = []
i = 0
while i < 10:
    lst.append(int(input('Enter a number: ')))
    i += 1

new_lst = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]

print(new_lst)