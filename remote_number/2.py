import random

lst = []
for i in range(1, 20):
    lst.append(random.randint(0, 9))
print(lst)

lstrem = []
for i in range(0, 20):
    lst.append(random.randint(0, 9))
print(lst)
for b in range(0, len(lst)):
    if lst[b] == 3:
        lstrem.append(b)
print(lstrem)
lstrem.reverse()
for c in lstrem:
    lst.pop(c)
print(lst)
