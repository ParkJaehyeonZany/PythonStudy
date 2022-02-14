listnum = [10,5,7,21,4,8,18]
listnum1 = listnum[1:]
listnum1.append(listnum[0])

for max in listnum:
    for b in listnum1:
        if max < b:
            max = b

for min in listnum:
    for b in listnum1:
        if min > b:
            min = b

print('max :', max, 'min :', min)

