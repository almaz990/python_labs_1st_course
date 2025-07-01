a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

if a <= b and a <= c:
    print('Минимальное значение равно', a)
elif b <= a and b <= c:
    print('Минимальное значение равно', b)
elif c <= a and c <= b:
    print('Минимальное значение равно', c)