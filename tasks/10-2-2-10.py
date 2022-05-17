original10 = int(input("input number:"))
print(original10)
lst =[]
reversed10 = 0
while original10 >= 1:
    original10,b = divmod(original10,2)
    if b != 0:
        lst.append(1)
    else:
        lst.append(0)
reversed2 = "".join([str(i) for i in lst])
reversed10 = 0
for i in range(0, len(lst)):
    reversed10 = reversed10*2 + lst[i]
lst.reverse()
original2 = "".join([str(i) for i in lst])
print(original2)
print(reversed2)
print(reversed10)