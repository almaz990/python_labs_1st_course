a, b = int(input('Enter a: ')), int(input('Enter b: '))
d = max(a, b)
for i in range(max(a,b), 0, -1):
    if a % i == 0 and b % i ==0:
        d = i
        break
print(f'd = {d}')