#特殊屬性與特殊方法

#__doc__特殊屬性:可以用來印出註解,或一些程式碼的說明

class Myclass:
    ''' 文檔字串實例'''
    def __init__(self, x):
        self.x = x
    def printMe(self):
        '''Myclass類別內printMe方法的應用'''
        print("Hi", self.x)

data = Myclass(100)
data.printMe()
print(data.__doc__)
print(data.printMe.__doc__)

#__str__()與__repr__()特殊方法
#__str__()可以讓print(類別)輸出適合閱讀的結果

class Name:
    def __init__(self, name):
        self.name = name

a = Name('Hung')
print(a)    #會輸出記憶體位置等相關訊息
a

'''如果再shell直接輸入a,會得到記憶體位置相關的訊息
這是因為系統是呼叫__repr__()方法做回應
要定義__repr__()方法'''

class Name2(Name):
    def __str__(self):
        return '%s' % self.name
    __repr__ = __str__  #定義__repr__()方法

a = Name2('Hung')
print(a)    


