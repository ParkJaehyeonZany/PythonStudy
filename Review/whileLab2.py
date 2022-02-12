import random

while True:
    pairNum1 = random.randint(1,6)
    pairNum2 = random.randint(1,6)
    if pairNum1 > pairNum2:
        print(f"{pairNum1} is bigger than {pairNum2}.")
    elif pairNum1 < pairNum2:
        print(f"{pairNum1} is smaller than {pairNum2}.")
    elif pairNum1 == pairNum2:
        print('Game Over')
        break