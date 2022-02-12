"""
숫자 야구
1. 0~9까지 랜덤한 숫자를 반복 없이 사용 하여 추출한다.
2. 숫자를 입력한다.
3. 숫자와 자리의 위치가 맞으면 STRIKE, 숫자만 맞으면 BALL을 출력하게 한다.
    단, 숫자가 하나도 맞지않는 경우는 OUT.
4. 맞춘 경우, 'YOU WIN'을 출력한다.
    10회 이상 정답을 못 맞출 경우, 'YOU LOSE'를 출력한다.
"""

import random

# 1. 0~9까지 랜덤한 숫자를 반복 없이 사용 하여 추출한다.
resultSet = list()
while True :
    if len(resultSet) == 3:
        break
    else :
        result = random.randint(0,9)
        if result in resultSet:
            continue
        else :
            resultSet.append(result)
print(resultSet) # 답

# 2. 숫자를 입력한다.
count = 0
while True:
    if count == 0:
        print('게임을 시작합니다!! 10턴 안에 게임을 끝내주세요.')
    elif count == 9:
        print(f"목숨 : {(10 - count)*'*'}\n마지막 차례입니다.")
    else:
        print(f"목숨 : {(10 - count)*'*'}")
    count += 1
    player = tuple(map(int, input('숫자를 입력하세요 : ').split()))
    if len(player) != 3 :
        while True:
            print('숫자 3개만 입력하세요 ex)')
            player = tuple(map(int, input('숫자를 입력하세요 : ').split()))
            if len(player) == 3:
                break

# 3. 숫자와 자리의 위치가 맞으면 STRIKE, 숫자만 맞으면 BALL을 출력하게 한다.
#    단, 숫자가 하나도 맞지 않는 경우는 OUT.
    strike = 0
    ball = 0
    for j in range(3):
        if resultSet[j] == player[j]:
            strike += 1
        else:
            for i in range(3):
                if resultSet[j] == player[i]:
                    ball += 1

# 4. 맞춘 경우, 'YOU WIN'을 출력한다.
#    10회 이상 정답을 못 맞출 경우, 'YOU LOSE'를 출력한다.
    if strike == 0 and ball == 0:
        print('OUT')
    elif strike == 3:
        print()
        print('YOU WIN!!!!')
        break
    else:
        print(f"{strike} STRIKE, {ball} BALL")
    print()
    if count == 10:
        print('YOU LOSE..')
        break
print('게임이 끝났습니다.')