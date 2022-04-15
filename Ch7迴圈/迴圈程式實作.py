#計算一給定數字以下的總和

n = int(input("請輸入整數:"))
number = list(range(n + 1))
total = 0

for i in number:
    total += i
    
print("從1到%d的總和 = " %n, total)

#建立平方數的串列

squares = []
n = int(input("請輸入整數"))

for num in range(1, n+1):
    squares.append(num ** 2)    #平方
    
print(squares)

#另一種建立平方數串列的方法

n = int(input("請輸入整數"))
squares = [num ** 2 for num in range(1, n+1)]
print(squares)

#列印99乘法表

for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end = " ") #靠左輸出
    print()     #由於python的迴圈是看縮牌來做的,因此這一行是屬於第一個for的   

#印金字塔
n = int(input("請輸入整數"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i:
            print("a", end = "")
    print()     #換行輸出


#印金字打精簡版    
n = int(input("請輸入整數"))
for i in range(1,n+1):
    print("a" * i, end = "")
    print()     #換行輸出

