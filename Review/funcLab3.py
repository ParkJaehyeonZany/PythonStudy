def expr(n1, n2, oper):
    if oper == '+':
        result = n1 + n2
    elif oper == '-':
        result = n1 - n2
    elif oper == '*':
        result = n1 * n2
    elif oper == '/':
        result = n1 / n2
    else:
        result = None
    return result

n1, n2 = map(int,input('Type n1 n2 : ').split())
oper = str(input('Type Oper : '))

result = expr(n1, n2, oper)

if result == None:
    print("Fail")
else:
    print('Result :', result)