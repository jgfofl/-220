import random

n = 28
a = []
for i in range(n):
    a.append(random.randint(0, 100))

min = 101
for i in a:
    if i >= 40 and i < min:
        min = i
print(a)
print(i)

