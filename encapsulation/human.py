class Human(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        print('응애응애')

    def who(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}')

    def setInfo(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human('조아름', 25, '여자')
areum.who()