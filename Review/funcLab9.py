def isPYTHON(*q):
    if q == ['PYTHON'] in q:
        return True
    else:
        return False

isPYTHON('나는 PYTHON을 학습합니다.')
if isPYTHON:
    print('PYTHON이 존재합니다.')
elif isPYTHON == False:
    print('PYTHON이 존재하지 않습니다.')