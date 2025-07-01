A, B, H, = int(input('Enter A: ')), int(input('Enter B: ')), int(input('Enter H: '))

if A <= H and H <= B: print('Здоровье')
elif H < A: print('Недосып')
elif H > B: print('Пересып')