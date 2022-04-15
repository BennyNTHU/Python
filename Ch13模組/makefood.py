#模組:講白一點就是套件,類似於C和C++的library
#這份檔案是一個自訂的模組makefood.py,順序上是第1個

def make_icecream(*toppings):
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

def make_drink(size, drink):
    print("所點飲料如下")
    print("--- ", size.title())
    print("--- ", drink.title())
