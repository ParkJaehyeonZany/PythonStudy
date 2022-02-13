def print_gugudan(num):
    if type(num) != int:
        return
    elif not 1 <= num <= 9:
        return
    else:
        for i in range(1,10):
            print(f"{num} * {i} = {num*i}")

for i in range(1,10):
    print_gugudan(i)
    print('-'*10)