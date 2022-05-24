import random

n = 30
a = []
for i in range(n):
    a.append(random.randint(-1000, 1000))

x = int(input("ВВедите число: "))

for i in a:
    if i == x:
        print(a[i])
    else:
        print("такого элемента нет")