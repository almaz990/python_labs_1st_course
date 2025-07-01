lst = [int(i) for i in input().split()]
x = int(input('Enter x: '))

if x not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if x == lst[i]:
            print(i, end=' ')
