string = input('Введите состав: ')
G_count = string.upper().count('G')
C_count = string.upper().count('C')
percent = (G_count + C_count) / len(string) * 100

print(f'Содержание GC равно {percent} %')