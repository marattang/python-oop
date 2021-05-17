class Bmi:

    def setState(self, hei, wei):
        self.hei = hei
        self.wei = wei

    def bmiCal(self):
        hei_2 = self.hei / 100
        return self.wei / (hei_2 * hei_2)

if __name__ == '__main__':
    b = Bmi()
    b.setState(155, 52)
    print(b.bmiCal())