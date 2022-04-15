#類別的封裝
#類別的屬性與方法有public(公開)與private(私有)兩種,私有屬性無法從外部更改
#而私有方法無法被類別外的程式調用
#宣告私有的方式是在成員前面加兩條底線__

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

hungbank = Banks('hung')                #建構元,定義物件hungbank
hungbank.get_balance()
hungbank.balance = 10000                #自外竄改
hungbank.get_balance()                  #會發現沒有作用

usdallor = 50
print(usdallor, "美金可以兌換", hungbank.usa_to_taiwan(usdallor), " 台幣")
