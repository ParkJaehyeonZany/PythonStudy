import random

oper_num = random.randint(1, 10)
if oper_num % 5 == 1:
    oper = 300+50
elif oper_num % 5 == 2:
    oper = 300-50
elif oper_num % 5 == 3:
    oper = 300*50
elif oper_num % 5 == 4:
    oper = 300/50
elif oper_num % 5 == 0:
    oper = 300%50
print(f"result : {oper}")