import random

listnum = []

for i in range(10):
    ranNum = random.randint(1,50)
    listnum.append(ranNum)
print(listnum)

for i in range(len(listnum)):
    if listnum[i] < 10:
        listnum[i] = 100
print(listnum)

print(listnum[0])
print(listnum[-1])
print(listnum[1:6])
print(listnum[::-1])
print(listnum[:])
del(listnum[4])
print(listnum)
listnum[1:3] =[]
print(listnum)
