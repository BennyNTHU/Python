#Python的函數再傳遞參數時不向C一樣還要管他是甚麼資料型態
#只要按照順序擺就可以了

def playball(name):
    print("%s打球" % name)

def dothing(name, activity, times):
    print(name + activity, t, "小時")
    
playball('丁文淵')

name = input('name')
act = input('做事')
t = input('多久')
dothing(name, act, t)   #參數記得要按照順序放,不然會跑出奇怪的結果

