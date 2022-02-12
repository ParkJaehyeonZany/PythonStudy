import random

ranNum = random.randint(5,10)
count = 0
while True:
    count += 1
    print(f"{count} -> {count**2}")
    if count == ranNum:
        break