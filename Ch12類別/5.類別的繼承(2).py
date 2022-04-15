#利用super()取得基礎類別方法
#當在衍生類別的方法中引用上一層基礎類別的方法時,需使用super()

class Grandfather():    #建立祖父類別
    def __init__(self):
        self.grandfathermoney = 10000
    def get_info1(self):
        print("Grandfather's information")

class Father(Grandfather):  #建立Father類別,繼承了GrandFather類別
    def __init__(self):
        self.fathermoney = 8000
        super().__init__()  #呼叫GrandFather類別的建構子,以取得GrandFather類別的屬性
    def get_info2(self):
        print("Father's information")

class Ivan(Father): #建立Ivan類別,繼承了Father類別
    def __init__(self):
       self.ivanmoney = 3000
       super().__init__()   #呼叫Father類別的建構子,以取得Father類別的屬性
    def get_info3(self):
        print("Ivan's information")
    def get_money(self):
        print("\nIvan資產: ", self.ivanmoney, "\n父親資產: ", self.fathermoney,
              "\n祖父資產: ", self.grandfathermoney)

ivan = Ivan()
ivan.get_info3()
ivan.get_info2()
ivan.get_info1()
ivan.get_money()
