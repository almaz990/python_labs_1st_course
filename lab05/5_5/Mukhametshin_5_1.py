lst = [int(i) for i in input('Enter numbers: ').split()]
x = int(input('Enter x: '))
str = ''
for i in range(len(lst) - 1):
    if lst[i] == x:
       str += f'{i} '
print(str)