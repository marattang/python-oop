class Grade:

    def setGrade(self, mat, eng, kor):
        self.mat = mat
        self.eng = eng
        self.kor = kor

    def sum(self):
        return self.mat+self.eng+self.kor

    def avg(self):
        return self.sum()/3

if __name__ == '__main__':
    g = Grade()
    g.setGrade(90, 85, 78)
    print(g.avg())
    print(g.sum())


class bmi:

    def setState(self,hei , wei):
        self.hei = hei
        self.wei = wei

    def bmiCal(self):
        return self.hei/(self.wei*self.wei)

