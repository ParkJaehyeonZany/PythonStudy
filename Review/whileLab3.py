import random

count = 0
while True:
    ranNum = random.randint(0,30)
    if ranNum == 0 or ranNum >= 27:
        print(f"The count is {count}")
        break
    upperStr = chr(ranNum+64)
    print(f"{upperStr}({ranNum})")
    count += 1



