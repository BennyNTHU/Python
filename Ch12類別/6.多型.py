#多型:個個類別間有相同方法名稱的狀況,這種情形與類別間是否有繼承狀況無關
#程式會由物件自動判斷該用哪一個方法去回應
#此程式顯示了which()函數的多型

class Animals():    #基礎類別
    def __init__(self, animal_name):    #基礎類別建構子
        self.name = animal_name
    def which(self):
        return 'My pet ' + self.name.title()
    def action(self):
        return ' sleeping'

class Dogs(Animals):    #衍生類別:有繼承which()函數,所以丟到doing()是可以的
    def __init__(self, dog_name):
        super().__init__(dog_name.title())  #呼叫基礎類別建構子
    def action(self):
        return ' running'

class Monkeys():    #其他類別
    def __init__(self, monkey_name):
        self.name = 'My monkey ' + monkey_name.title()
    def which(self):
        return self.name
    def action(self):
        return ' jumping'

def doing(obj): #以類別作為物件的函數
    print(obj.which(), "is", obj.action())

my_cat = Animals('lucy')
doing(my_cat)
my_dog = Dogs('gimi')
doing(my_dog)
my_monkey = Monkeys('taylor')
doing(my_monkey)
