a = float(input('Enter a: '))
b = float(input('Enter b: '))
operation = input('Enter operation: ')
if operation == '+': print(f'Result: {a + b}')
elif operation == '-': print(f'Result: {a - b}')
elif operation == '/':
    if b != 0.0:
        print(f'Result: {a / b}')
    else:
        print('Деление на 0!')
elif operation == '*': print(f'Result: {a * b}')
elif operation == 'mod' or operation == '%': print(f'Result: {a % b}')
elif operation == 'pow' or operation == '**': print(f'Result: {a ** b}')
elif operation == 'div' or operation == '//':
    if b != 0.0:
        print(f'Result: {a // b}')
    else:
        print('Деление на 0!')