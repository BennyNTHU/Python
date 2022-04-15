#類別模組

class Banks():
    def __init__(self, uname):          
        self.__name = uname             
        self.__balance = 0             
        self.__title = 'Taipei Bank'
        
    def save_money(self, money):        #定義存款方法
        self.__balance += money
        print("存款 ", money, " 完成")

    def withdraw_money(self, money):    #定義提款方法
        self.__balance -= money
        print("提款 ", money, " 完成")
    
    def get_balance(self):              #定義存款查詢方法
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def bank_title(self):               #取得私有屬性的方法
        return self.__title

class Shilin_Banks(Banks):      #繼承了Banks類別
    def __init__(self, uname):  #衍生類別自己的建構子  
        self.title = "Taipei bank - Shilin Branch"
    def bank_title(self):
        return self.title   #跟基礎類別有相同名稱的屬性,會看你是叫誰
