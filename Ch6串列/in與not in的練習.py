#in:用來判斷一物件是否在另一物件之中
#物件可以是字串,串列,元組或字典

password = 'deepstone'
ch = input("請輸入字元 = ")

if ch in password:
    print("輸入字元在密碼中")
else:
    print("輸入字元不在密碼中")

judge = ch in password
print(judge, type(judge))   #藉由in得到的資料型態是boolean

#not in:可用來判斷一物件是否不位於另一物件之中

password2 = 'python'
ch = input("請輸入字元 = ")

if ch not in password:  
    print("輸入字元不在密碼中")
else:
    print("輸入字元在密碼中")

judge = ch not in password
print(judge, type(judge))

#另一個練習

fruit_like = ['apple', 'banana', 'watermelon']
fruit = input("請輸入水果")

if fruit in fruit_like:
    print("這個水果已經有了")
else:
    fruit_like.append(fruit)
    print("已加入水果清單中:", fruit_like)
