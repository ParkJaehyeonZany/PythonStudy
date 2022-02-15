l = [
    ['B', 'C', 'A', 'A'],
    ['C', 'C', 'B', 'B'],
    ['D', 'A', 'A', 'D']
]

l_count =[]
for j in range(4):
    sum = 0
    str = chr(65+j)
    for i in range(len(l)):
        c = l[i].count(str)
        sum += c
    print(f"{str}counts are {sum}")