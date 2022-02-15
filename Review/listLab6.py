l = [
    [10,12,14,16],
    [18,20,22,24],
    [26,28,30,32],
    [34,36,38,40]
]

print('Row 1, Column 1 : ', l[0][0])
print('Row 3, Column 4 : ', l[2][3])
print('Count Row : ', len(l))
print('Count column : ', len(l[0]))
print('Data of Row 3 : ', *l[2])
print('Data of Column 2: ', end='')
for i in range(len(l[1])):
    print(l[i][1], end=' ')
print()
print('Date of diagonally to the left : ', end='')
for i in range(4):
    for j in range(4):
        if i == j:
            print(l[i][j], end=' ')
print()
print('Date of diagonally to the right : ', l[0][3], l[1][2], l[2][1], l[3][0])
