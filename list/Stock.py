class Stock(object):
    def __init__(self, stock_name, stock_id):
        self.stock_name = stock_name
        self.stock_id = stock_id

    def to_String(self): #to_String
        return f'종목 이름 : {self.stock_name} 종목 코드 : {self.stock_id}'

    @staticmethod
    def del_element(stock_list, code):
        for i, j in enumerate(stock_list):
            if j.stock_id == code:
                del stock_list[i]

    @staticmethod
    def main():
        stock_list = []
        while 1:
            option = input('옵션을 선택하세요. 0. 종료 1. 종목 추가 입력 2. 종목 조회 3. 삭제 4.수정')
            i = 0
            if option == '0':
                break
            elif option == '1':
                stock_list.append(Stock(input('종목명을 입력하세요.'), input('종목코드를 입력하세요.')))
            elif option == '2':
                for i in stock_list:
                    print(i.to_String())
            elif option == '3':
                Stock.del_element(stock_list, input('삭제할 종목코드 입력.'))
            elif option == '4': #1회 이상 사용되는 변수는 선언되어야 함. 두번 사용해서 code 변수 선언
                code = input('삭제할 종목코드 입력.')
                stock = Stock(input('수정할 이름'), code)
                stock.del_element(stock_list, code)
                stock_list.append(stock)
            else :
                continue

Stock.main()