l = [
    [10,20,30,40,50],
    [5,10,15],
    [11,22,33,44],
    [9,8,7,6,5,4,3,2,13]
]

count = 0
for i in l:
    sum = 0
    count += 1
    for j in i:
        sum += j
    print(f"Sum of Row {count} : {sum}")