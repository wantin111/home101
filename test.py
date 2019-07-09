class Test:
    def __init__(self,num):
        self.num=num;
    def print_num(self):
        print('引数で渡された数字は{}です。'.format(self.num)) 
    def __del__(self):
        print('デストラクタが呼ばれました')

test = Test(10)  #インスタンスを生成
test.print_num() 
del test      #インスタンスを削除