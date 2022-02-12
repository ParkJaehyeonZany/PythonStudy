num = int(input('write number (1~10) : '))
if not 1 <= num <= 10:
    print("It isn't between 1 and 10.")
else:
    if num % 2 == 0:
        print("Even number.")
    else:
        print("Odd number.")