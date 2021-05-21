import random

class Account(object):
    # 생성자 함수.
    def __init__(self, acct_cu, acct_amt):
        self.bank = 'SC은행' #상수 대문자
        self.acct_no = self.create_acc_number()
        self.acct_cu = acct_cu
        self.acct_amt = acct_amt

    @staticmethod
    def create_acc_number():
        count = (3, 2, 6)
        acct_no = ''
        for i in range(3):
            for j in range(count[i]):
                num = str(random.randint(0, 9))
                acct_no += num
            if i < 2:
                acct_no += '-'
        return acct_no

    def account_info(self):
        return f'은행이름 : {self.bank} ,' \
               f'계좌번호 : {self.acct_no},' \
               f' 계좌주 : {self.acct_cu},' \
               f' 잔액 : {self.acct_amt}'
    
    # 입금 횟수
    depo_account = {}

    def deposit(self):
        acct_amt = int(input('입금할 금액을 입력해주세요'))
        act = '입금'
        if acct_amt >= 1:

            for i in self.depo_account:
                    self.depo_account[i] = self.depo_account[i] + 1
                    if self.depo_account[i]%5 == 0:
                        print(f'{self.acct_cu}고객의 계좌로 이자 {self.acct_amt}*0.01 원이 입금되었습니다.')
                        self.acct_amt = self.acct_amt + self.acct_amt * 0.01

            self.acct_amt = acct_amt + self.acct_amt
            self.account_history(acct_amt, act)
        else:
            print('금액은 1원 이상 입력해주셔야 합니다.')
        return self.acct_amt

    def withdraw(self):
        acct_amt = int(input('출금할 금액을 입력해주세요'))
        act = '출금'
        if acct_amt >= 1:
            if self.acct_amt < acct_amt :
                print('잔액이 부족합니다')
            else :
                self.acct_amt = self.acct_amt - acct_amt
                self.account_history(acct_amt, act)
        else:
            print('금액은 1원 이상 입력해주셔야 합니다.')
        return self.acct_amt

    def account_history(self, acct_amt, act):
        print(f'{acct_amt}원 만큼 {act}합니다.')
        print(f'{self.acct_cu}고객의 잔액은 {self.acct_amt}원 입니다.')

    @staticmethod
    def acct_check(option, acct_list, acct_no):
        for i in acct_list:
            if acct_no == i.acct_no:
                if option == '3':
                    i.deposit()
                elif option == '4':
                    i.withdraw()
                elif option == '5':
                    return acct_no
            else:
                print('해당하는 계좌주가 없습니다.')
                break

    @staticmethod
    def main():
        acct_list = []
        depo_account = {}

        while 1:
            option = input('0. 종료 1. 은행 계좌 추가 2. 은행 계좌 조회 3.입금 4. 출금 5.계좌 삭제')
            if option == '0':
                break

            elif option == '1':
                acct_cu = input('예금주를 입력해주세요')
                acct_list.append(Account(acct_cu, int(input('입금할 금액을 입력해주세요'))))
                Account.depo_account[f'{acct_cu}'] = 1

            elif option == '2':
                for i in acct_list:
                    print(i.account_info())

            elif option == '3':
                Account.acct_check(option, acct_list, input('계좌 번호를 입력해주세요.'))
                        
            elif option == '4':
                Account.acct_check(option, acct_list, input('계좌 번호를 입력해주세요.'))

            elif option == '5':
                acct_no = input('계좌 번호를 입력해주세요.')
                Account.acct_check(option, acct_list, acct_no)
                for i, j in enumerate(acct_list):
                    if acct_no == j.acct_no:
                        del acct_list[i]

            else :
                print("메뉴를 다시 입력해주세요.")
                continue

        print('잔액이 100만원 이상인 고객 계좌 추출')
        for i in acct_list:
            if i.acct_amt >= 1000000:
                print(i.account_info())
            else:
                pass

Account.main()
