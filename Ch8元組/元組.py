#元組:
#元組就是不可更改個數與內容的串列
#其優點是資料結構較為簡單,執行迅速
#我們利用小括號()宣告元組

numbers = (1,2,3,4,5)
fruits = ('banana', 'orrange', 'watermelon', 'grape', 'strawberry')
mixed = ('Capoo', 26, 'F')      #元組可包含混合資料型態
val = (10,) #只含一元素的元組
print(type(numbers))

#讀取原組資料
print(fruits[0])
print(numbers[3])
print(mixed[2])

for fruit in fruits:    #利用迴圈讀取元組資料
    print(fruit)

print(fruits[1:3])      #列印fruits[1]到fruits[2]
print(fruits[:2])       #列印fruits[0]到fruits[1]
print(fruits[1:])       #列印fruits[1]到fruits最後一個元素
print(fruits[-2:])      #列印fruits倒數第二個元素到最後一個元素
print(fruits[0:5:2])    #從fruits[0]到fruits[4],每隔2元素列印一次

#修改元組元素會出現錯誤,但元組本身可以用全新定義方式去修改
'''
fruits[0] = 'banana'
fruits.pop('banana')
fruits.append('Capoo')
'''

#可用在元組的函數
print("fruits的元素個數 = ", len(fruits))    #求元素個數
print("num最大值是", max(numbers))  #求最大最小值
print("num最小值是", min(numbers))
