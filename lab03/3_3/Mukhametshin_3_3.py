a = [int(s) for s in input('Enter numbers: ').split()]

print(f'Среднее арифметическое равно {int(sum(a)/len(a))}')
print(f'Всего значений больше среднего арифметического: {len([int(x) for x in a if x > int(sum(a)/len(a))])}')
print(f'Список значений: {[int(x) for x in a if x > int(sum(a)/len(a))]}')