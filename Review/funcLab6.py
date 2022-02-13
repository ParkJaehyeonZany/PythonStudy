import random

def differtwovalue(n1,n2):
    if n1 >= n2:
        result = n1 - n2
    elif n2 > n1:
        result = n2 - n1
    return result

for i in range(5):
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    print(f"The difference between {num1} and {num2} is {differtwovalue(num1,num2)}.")