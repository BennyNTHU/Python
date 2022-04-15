'''
Python類別的建構子跟C++的很像,可藉由它來宣告(初始化)一個類別物件
建構元為__init__(),需注意左右兩邊各是兩條底線
self是所有方法中必要的參數,有點像C++中的this指標
Python在初始化時會自動傳入這個參數self
當你想在類別內存取各屬性與各方法時,皆要使用self
'''

class Banks():
    title = 'Taipei Bank'
    def __init__(self, uname, money):   #建構元(初始化方法)
        self.name = uname               #設定屬性name
        self.balance = money            #設定屬性money

    def save_money(self, money):        #定義存款方法
        self.balance += money
        print("存款 ", money, " 完成")

    def withdraw_money(self, money):    #定義提款方法
        self.balance -= money
        print("提款 ", money, " 完成")
    
    def get_balance(self):              #定義存款查詢方法
        print(self.name.title(), " 目前餘額: ", self.balance)

hungbank = Banks('hung', 100)           #建構元,定義物件hungbank
hungbank.get_balance()
hungbank.save_money(300)
hungbank.get_balance()
hungbank.withdraw_money(200)
hungbank.get_balance()
