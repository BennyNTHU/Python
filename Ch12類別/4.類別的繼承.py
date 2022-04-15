#類別的繼承
'''
Python的繼承有以下幾點特性
1.父類別(基底類別)的所有公有屬性與供有方法都可以被繼承,直接引用
2.無法存取父類別的私有屬性
3.當衍生類別的屬性或方法名稱與基底類別重複時,會以衍生類別為優先
'''

class Banks():
    def __init__(self, uname):          #建構元
        self.__name = uname             #設定私有屬性name
        self.__balance = 0              #設定私有屬性balance初始值為0
        self.__title = 'Taipei Bank'
        self.__rate = 30                #美金與台幣換兌比率
        self.__service_charge = 0.01    #換兌服務費

    def save_money(self, money):        #定義存款方法
        self.__balance += money
        print("存款 ", money, " 完成")

    def withdraw_money(self, money):    #定義提款方法
        self.__balance -= money
        print("提款 ", money, " 完成")
    
    def get_balance(self):              #定義存款查詢方法
        print(self.__name.title(), " 目前餘額: ", self.__balance)

    def usa_to_taiwan(self, usa_d):
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self, usa_d):        #定義私有方法
        return int(usa_d * self.__rate * (1-self.__service_charge))
    
    def bank_title(self):               #取得私有屬性的方法
        return self.__title

class Shilin_Banks(Banks):      #繼承了Banks類別
    def __init__(self, uname):  #衍生類別自己的建構子  
        self.title = "Taipei bank - Shilin Branch"
    def bank_title(self):
        return self.title   #跟基礎類別有相同名稱的屬性,會看你是叫誰

jamesbank = Banks('James')
print("James banks = ", jamesbank.bank_title()) #呼叫衍生類別的bank_title()方法
hungbank = Shilin_Banks('Hung')
print("Hung's banks = ", hungbank.bank_title()) #呼叫基礎類別的bank_title()方法

