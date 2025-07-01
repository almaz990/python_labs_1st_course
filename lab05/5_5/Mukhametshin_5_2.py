matrica = [[int(j) for j in input('Enter j: ').split()] for i in range(3)]


for i in range(3):
    print()
    for j in range(3):
        print(matrica[i][j], end=' ')

new_matrica = []

for i in range(2):

    for j in range(2):
        new_matrica.append(matrica[i - 1][j] + matrica[i + 1][j] + matrica[i][j - 1] + matrica[i][j + 1])


print(new_matrica)