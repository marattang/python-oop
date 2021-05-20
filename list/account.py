import random


class Account(object):
    def __init__(self, acct_cu, acct_amt):
        self.bank = 'SC은행'
        self.acct_no = str(random.randrange(100, 1000)) + '-' + str(random.randrange(1, 100)).zfill(2) + '-' + str(random.randrange(100000, 1000000))
        self.acct_cu = acct_cu
        self.acct_amt = acct_amt

    def account_info(self):
        return f'은행이름 : {self.bank} 계좌번호 : {self.acct_no} 계좌주 : {self.acct_no} 잔액 : {self.acct_amt}'

    count = 0

    def deposit(self):
        acct_amt = int(input('입금할 금액을 입력해주세요'))
        if acct_amt >= 1:
            self.acct_amt = acct_amt + self.acct_amt
        else:
            print('금액은 1원 이상 입력해주셔야 합니다.')

    def withdraw(self):
        acct_amt = int(input('출금함 금액을 입력해주세요'))
        if acct_amt >= 1:
            if self.acct_amt < acct_amt :
                print('잔액이 부족합니다')
            else :
                self.acct_amt = self.acct_amt - acct_amt
                print(f'{acct_amt}원 만큼 출금합니다.')
                print(f'잔액은 {self.acct_amt}원 입니다.')
        else:
            print('금액은 1원 이상 입력해주셔야 합니다.')
        return self.acct_amt

    @staticmethod
    def main():
        acct_list = []

        while 1:
            option = input('0. 종료 1. 은행 계좌 추가 2. 은행 계좌 조회 3.입금 4. 출금')
            if option == '0':
                break

            elif option == '1':
                acct_list.append(Account(input('예금주를 입력해주세요'), int(input('입금할 금액을 입력해주세요'))))

            elif option == '2':
                for i in acct_list:
                    print(i.account_info())

            elif option == '3':
                depo_act = input('입금할 계좌의 계좌주를 입력해주세요.')

            elif option == '4':
                with_act = input('출금할 계좌의 계좌주를 입력해주세요.')

            else :
                print("다시 입력해주세요.")
                continue




Account.main()