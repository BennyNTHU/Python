#Python可以一次回傳多筆資料,回傳值的資料型態也不需要相同

#沒有回傳值的函數,回傳None給主程式
#相當於C的void()
def greeting(name):
    print("Hi, ", name)

#如果加上return,結果是一樣的
def greeting2(name):
    print("Hi, ", name)
    return

ret = greeting('Benny')
print("greeting()的資料型態: ", type(greeting))
print("greeting()的回傳值: ", ret)
print("回傳值的資料型態: ", type(ret))

ret2 = greeting2('Benny')
print("greeting2()的資料型態: ", type(greeting2))
print("greeting2()的回傳值: ", ret2)
print("回傳值的資料型態: ", type(ret2))
