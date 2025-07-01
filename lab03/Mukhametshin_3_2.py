n = int(input('Enter n: '))
count = 0
for i in range(n + 1):
    if count == n: break
    for j in range(i):
        print(i, end=' ')
        count += 1
        if count == n: break