def print_triangle(num):
    if 1 <= num <= 10:
        for i in range(1,num+1):
            print('*'*(num-i+1), sep='')
    else:
        return

print_triangle(5)