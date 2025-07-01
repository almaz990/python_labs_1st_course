cost = 1500
N, M = int(input("Enter N: ")), int(input("Enter M: "))
K = N * cost * (1 - M / 100)
print(f"Стоимость {N} шт. товаров составляет {K} руб. с учетом скидки {M}%")
