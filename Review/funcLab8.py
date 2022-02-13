def print_triangle_withdeco(num, deco='%'):
    if not 1 <= num <= 10:
        num = 5
    for i in range(1,num+1):
        print(' '*(num-i),deco*i,sep='')

print_triangle_withdeco(13)
