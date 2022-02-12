while True:
    num = int(input('Type number : '))
    mul = 1
    if num == 0:
        print("The End")
        break
    elif num < -10 or num > 10:
        continue
    elif num > 0:
        for i in range(1,num+1):
            mul = mul * i
        print(f'Input Result : {num}')
        print(mul)
    elif num < 0:
        num = num * (-1)
        for i in range(1,num+1):
            mul = mul * i
        print(f"Input Result(*-1)  : {num}")
        print(mul)