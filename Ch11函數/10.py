#其他事項

'''
區域變數與全域變數:
Python跟C類似。對Python而言,在主程式內就是全域變數
但是在函數內就是區域變數
全域變數可以被程式的任何函數在不經由參數傳遞的情形下呼叫,比方:
'''

def printmsg(): #沒有參數
    print("函數列印:", msg)

msg = 'msg是全域變數'
print("主程式列印:", msg)
printmsg()

#pass: 可以把pass還沒開始設計的函數

def fun():
    pass

fun()   #沒有執行結果

#函數的資料型態

print("fun函數的資料型態: ", type(fun))
print("匿名函數的資料型態: ", type(lambda x: x))
print("內建函數的資料型態: ", type(len))

#遞迴呼叫

def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

print("5! = ", factorial(5))
