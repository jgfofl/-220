import random

n = 20
a = []
for i in range(n):
    a.append(random.randint(0, 1000))
min = 1001
for i in a:
    if i % 2 == 0 and i % 3 == 0 and i < min:
        min = i
print(a)
print(min)