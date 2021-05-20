class Grade: #class

    def __init__(self, mat, eng, kor):   #setter
        self.mat = mat #프로퍼티 : 변수의 종류
        self.eng = eng
        self.kor = kor

    def sum(self):
        return self.mat+self.eng+self.kor #getter 서브루틴이기 때문에 self만 있고 다른 매개변수는 없음.

    def avg(self):
        return self.sum()/3

    @staticmethod
    def main():
        g = Grade(int(input('수학점수 :')), int(input('영어점수 :')), int(input('국어점수 :')))

        print(f'평균: {g.avg()}')
        print(f'총점: {g.sum()}')
        print(f'학점: {g.get_grade()}')

    def get_grade(self):
        score = int(self.avg())
        if score >= 90:
            grade = 'A 학점'
        elif score >= 80:
            grade = 'B 학점'
        elif score >= 70:
            grade = 'C 학점'
        elif score >= 60:
            grade = 'D 학점'
        elif score >= 50:
            grade = 'E 학점'
        else :
            grade = 'F 학점'
        return grade

Grade.main()

