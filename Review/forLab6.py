evenNum = 0
oddNum = 0

for num in range(1,101):
    if num % 2 == 0:
        evenNum += num
    else:
        oddNum += num

print('Out of the numbers from 1 to 100,')
print(f'Sum with the even numbers is {evenNum},')
print(f'Sum with the odd numbers is {oddNum}.')