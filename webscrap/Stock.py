import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Stock(object):
    url = ''
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    keyword = []
    rate = []

    def printRanking(self):

        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        count = 1
        for i in soup.find_all(name='tr'):
            if i.find("a") == None :
                pass
            else :
                self.keyword.append(i.find("a").text)
                print(type(i.find("a")))
                count += 1
            if type(i.find("span", class_="tah p11 red01")) == 'bs4.element.Tag':
                self.rate.append(i.find("span", class_="tah p11 red01").text.replace("\t", "\n").replace("\n", ""))
            elif type(i.find("span", class_="tah p11 nv01")) == 'bs4.element.Tag':
                self.rate.append(i.find("span", class_="tah p11 nv01").text.replace("\t", "\n").replace("\n", ""))
            elif type(i.find("span", class_="tah p11")) == 'bs4.element.Tag':
                self.rate.append(i.find("span", class_="tah p11").text.replace("\t", "\n").replace("\n", ""))
            else:
                pass


        for i in range(len(self.keyword)):
            print(f'{i}위 종목 : {self.keyword[i]} 등락률 : {self.rate[i]}')

# https://finance.naver.com/sise/lastsearch2.nhn
    @staticmethod
    def main():

        stock = Stock()

        while 1:
            menu = input('0.Exit 1.Input URL 2. PrintRanking')

            if menu == '0':
                break

            elif menu == '1':
                stock.url = input('Input URL')

            elif menu == '2':
                stock.printRanking()

            else:
                input('Wrong Number')

Stock.main()