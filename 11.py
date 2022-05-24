import random

n = 30
a = []
s = 0
j = 0
for i in range(n):
    a.append(random.randint(-1000, 1000))
for i in a :
    if i >= 0:
        s +=i
    if i < 0:
        j += 1
print(a)
print(s)
if j == 0:
    print("отрицательных элементов нет")
