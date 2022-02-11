class Account:
    def __init__(self, accountNo, ownerName, balance=0):
        self.accountNo = accountNo
        self.ownerName = ownerName
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

obj = [
    Account("111-222-1234567", "박재현", 50000),
    Account("222-333-7654321", "Zany", 100000),
    Account("333-444-1231231", "고길동", 3000)
]

accountNo = input('계좌를 입력하세요 : ')
ownerName = input('예금주 성함을 입력하세요 : ')

for i in obj:
    if accountNo == i.accountNo and ownerName == i.ownerName:
        print(f"잔액 : {i.balance:,}")
        if input('입금하시겠습니까? (y/n) ') == 'y' :
            amount = int(input('얼마를 입금하시겠습니까? '))
            i.deposit(amount)
            print(f"잔액 : {i.balance:,}")
        elif input('출금하시겠습니까? (y/n) ') == 'y' :
            amount = int(input('얼마를 출금하시겠습니까? '))
            i.withdraw(amount)
            if i.balance < 0 :
                print('잔액이 부족합니다.')
            else :
                print(f"잔액 : {i.balance:,}")
