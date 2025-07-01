string = input('Введите последовательность: ')
new_string = ""
cnt = 1
for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        cnt += 1
    elif string[i] != string[i + 1]:
        new_string += string[i]
        new_string += str(cnt)
        cnt = 1
    if i == len(string) - 2:
        new_string += string[i + 1]
        new_string += str(cnt)
print(new_string)