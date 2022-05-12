import random

lst = []
for i in range(1, 20):
    lst.append(random.randint(0, 9))
print(lst)

a = 0
while a < len(lst):
    if lst[a] != 3:
        a += 1
    else:
        lst.pop(a)
        a = a - 1
print(lst)
