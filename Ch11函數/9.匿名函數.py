#匿名函數是指一個沒有名稱的函數,用lambda定義之
#匿名函數可以有很多參數,但只能有一個表達式,然後傳回執行

square = lambda x: x ** 2   #回傳x的平方
print(square(10))   #呼叫匿名函數時,直接用所令的變數

product = lambda x, y: x * y
print(product(5, 10))

'''
匿名函數的功能有點類似C裡面的函數指標,因為匿名函數常常作為其他函數的參數
比方說我們想要篩出串列中的奇數,一般的寫法會使用filter函數
filter函數的有兩個參數,第一是一個函數,第二是串列,元組,字串等由元素組成的資料型態
filter會把串列的元素逐一丟到函數內,並把執行結果是True的元素組成新的物件傳回
'''

def oddfn(x):
    if (x % 2 == 1):
        return x
    else:
        return None

mylist = [5, 10, 15, 20, 25, 30]
filter_obj = filter(oddfn, mylist)  #把mylist的元素一個一個丟進oddfn檢測
odd_list = []
for item in filter_obj:
    odd_list.append(item)

print(odd_list)

#如果嫌這個程式碼太長,可以簡寫為
def oddfn(x):
    return x if (x % 2 == 1) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_obj = filter(oddfn, mylist)  #把mylist的元素一個一個丟進oddfn檢測
print([item for item in filter_obj])

#但如果用匿名函數去寫,就非常簡單
mylist = [5, 10, 15, 20, 25, 30]
odd_list = list(filter(lambda x: (x % 2 == 1), mylist))
print(odd_list)

#最喪心病狂的情形下可以一行寫完
print(list(filter(lambda x: (x % 2 == 1), [5, 10, 15, 20, 25, 30])))
