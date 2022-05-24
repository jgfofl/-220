import random

n = 50
a = []
for i in range(n):
    a.append(random.randint(-1000, 1000))

min = -1
j = 0
for i in a:
    if i < min:
        min = i
        j += 1

print(a)
print(min)
if j == 0:
    print("отрицательных жлементов нет")