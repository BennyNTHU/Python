#傳遞任意數量的參數:Python的函數可以傳遞任意數量的參數

def make_icecream(*toppings):    #可傳遞任意筆資料給參數toppings
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("---", topping)

make_icecream('牛奶')
make_icecream('牛奶', '空氣', '塑化劑') #全部傳給toppings

#甚至是說,如果參數列的參數不夠用,利用**可以在呼叫時自行增加
#此時任意數量的參數要放在最右邊

def build_dict(name, age, **players):
    info = {}
    info['Name'] = name
    info['Age'] = age
    
    for key, value in players.items():  #多的參數會被丟進這裡
        info[key] = value
    return info

player_dict = build_dict('James', '32', City = 'Cleveland', State = 'Ohio')
print(player_dict)
