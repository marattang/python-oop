'''
이름, 출생년도, 주소를 입력받아서
회원가입한 사람의 이름, 나이, 주소를 출력하시오
'''

class Person(object):

    def __init__(self, name, birth_year, address):
        self.name = name
        self.birth_year = birth_year
        self.address = address
    
    @staticmethod
    def main():
        p = Person(input('이름 : '), int(input('출생년도 : ')), input('주소 : '))
        p.birth_year
        age = 2021 - p.birth_year
        print('** 가입 정보 **')
        print(f'이름 : {p.name}')
        print(f'나이 : {age}')
        print(f'주소 : {p.address}')


Person.main()
