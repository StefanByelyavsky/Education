import random

lst = []
for i in range(1, 20):
    lst.append(random.randint(0, 9))
print(lst)

lst_filtered = []
for item in lst:
    if item != 3:
        lst_filtered.append(item)
print(lst_filtered)
