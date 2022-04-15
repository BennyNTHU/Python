#字典的定義
#字典是由"鍵(key)"與"值(value)"組合而成的資料結構,並用大括號宣告
#宣告方法dict_name = {鍵1:值1, 鍵2,值2, ...}
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print(fruits)
print("字典fruits的資料型態是: ", type(fruits))
print("水蜜桃一斤 = ", fruits['水蜜桃'], "元")

#增加字典元素
fruits['橘子'] = 18
print(fruits)

#更改字典內容
fruits['香蕉'] = 18
print("香蕉一斤新價格 = ", fruits['香蕉'], "元")
fruits['香蕉'] += 5
print("漲價後香蕉一斤價格 = ", fruits['香蕉'], "元")

#刪除字典元素
print("原本字典fruits內容: ", fruits)
del fruits['西瓜']
print("新的字典fruits內容: ", fruits)

#刪除字典所有元素
#會把字典所有元素刪掉變成一本空字典
fruits.clear()
print("清除字典後內容: ", fruits)

#刪除字典
del fruits
#print(fruits)   #會出現錯誤,因為此時fruits在記憶體已不存在

#建立空字典
noodles = {}
print(noodles)

noodles['牛肉麵'] = 100
noodles['肉絲麵'] = 80
noodles['陽春麵'] = 60
print(noodles)

#字典的複製
cnoodles = noodles.copy()
print("位址 = ", id(noodles), "noodles元素: ", noodles)
print("位址 = ", id(cnoodles), "cnoodles元素: ", cnoodles)  #位置會不一樣

#取得字典元素個數
print("noodles元素個數 = ", len(noodles))

#驗證元素是否存在
key = input("請輸入麵: ")
if key in noodles:
    print("%s 已經在字典中了" % key)
else:
    print("%s 不在字典中" % key)
