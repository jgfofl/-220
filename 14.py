import random

n = 40
a = []
for i in range(n):
    a.append(random.randint(-1000, 1000))

min = 1001
j = 0
for i in a:
    if i < min and i > 0 :
        min = i
        j += 1

print(a)
print(min)
if j == 0:
    print("положительных жлементов нет")