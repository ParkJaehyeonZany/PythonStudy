listnum = [10,5,7,21,4,8,18]
listnum1 = listnum[1:]
listnum1.append(listnum[0])

for a in listnum:
    for b in listnum1:
        if a < b:
            a = b

print('max :', a)