vremia = input('Введите время в формате HH:MM :')
lst = vremia.split(':')
chas = int(lst[0])
minuta = int(lst[1])
if chas >= 12:
    chas = chas - 12
gradC = chas * 30 + minuta * 0.5
gradM = minuta*6
delta = gradM - gradC
if delta >= 180:
    print(360 - delta)
else:
    print(delta)