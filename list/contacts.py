'''
이름, 전화번호, 이메일, 주소를 받아서 연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''

class Contacts(object):

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def print_contacts(self):
        return f'주소록 : 이름 {self.name}, 전화번호 {self.phone}, 이메일 {self.email}, 주소 {self.address}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('메뉴를 입력해주세요. 0.종료 1. 주소록 추가 2.출력 3.삭제 4.수정')
            if menu == '1':
                ls.append(Contacts(input('이름을 입력하시오'), input('전화번호를 입력하시오 '), input('이메일을 입력하세요'), input('주소를 입력하시오')))
            elif menu == '0':
                break
            elif menu == '2':
                for i in ls:
                    print(f'출력결과 : {i.print_contacts()}')
            elif menu == '3':
                del_name = input('삭제할 이름 : ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            elif menu == '4':
                re_name = input('수정할 이름 : ')
                for i, j in enumerate(ls):
                    if j.name == re_name:
                        

            else :
                print('다시 입력해주세요.')
                continue

Contacts.main()