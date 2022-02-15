import random

lotto = []
count = 0


num = random.randint(1,45)
lotto.append(num)

while count < 5:
    num = random.randint(1,45)
    x = True
    for j in range(len(lotto)):
        if lotto[j] == num:
            x = False
            break
    if x == False:
        continue
    lotto.append(num)
    count += 1

print('Lotto Numbers :', end='')
for i in range(len(lotto)):
    if i < len(lotto)-1:
        print(lotto[i],', ',sep='',end='')
    else :
        print(lotto[i])