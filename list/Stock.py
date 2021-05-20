class Stock():
    def __init__(self, stock_name, stock_id):
        self.stock_name = stock_name
        self.stock_id = stock_id

    def stock_info(self):
        return f'종목 이름 : {self.stock_name} 종목 코드 : {self.stock_id}'

    @staticmethod
    def main():

        stock_list = []
        while 1:
            option = input('옵션을 선택하세요. 0. 종료 1. 종목 추가 입력 2. 종목 조회 3. 삭제')
            i = 0
            if option == '1':
                stock_list.append(Stock(input('종목명을 입력하세요.'), input('종목코드를 입력하세요.')))
            elif option == '0':
                break
            elif option == '2':
                for i in stock_list:
                    print(i.stock_info())
            elif option == '3':
                del_stock = input('삭제할 종목을 입력하세요.')
                for i, j in enumerate(stock_list):
                    if j.stock_name == del_stock:
                        del stock_list[i]
            else :
                continue

Stock.main()