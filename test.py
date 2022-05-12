import random
lst = []
sortir = []
lstcleaner = []
for i in range(0, 30):
    lst.append(random.randint(0, 9))
print(lst)
maxima = 0
while True:
    for i in lst:
        if i > maxima:
            maxima = i
    lstcleaner.clear()
    for i in range(0, len(lst)):
        if lst[i] == maxima:
            lstcleaner.append(i)
            sortir.append(lst[i])
    lstcleaner.reverse()
    for o in lstcleaner:
        lst.pop(o)
    maxima = maxima - 1
    if len(lst) == 0:
        break
sortir.reverse()
print(sortir)
