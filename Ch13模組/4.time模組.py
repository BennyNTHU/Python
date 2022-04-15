#time()模組:
import time
import random

'''根據Micro Soft紀載,世界創始於1970年1月1日00:00:00
time()方法會回傳自該時刻以來的秒數'''
print("創世紀以來已經過 %d 秒" % int(time.time()))
      
#sleep():以秒為單位,讓工作暫停,主要應用在動畫繪製
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
   # time.sleep(1)    #每隔一秒列印一次

#asctime():列出目前系統時間
print(time.asctime())

#localtime():列出目前時間的結構資料
xtime = time.localtime()
print(xtime)
print("年 ", xtime[0])
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期 ", xtime[6])
print("一年中第幾天 ", xtime[7])
print("是否有夏令時間 ", xtime[8])

#設計一個猜數字的小遊戲,可以看你花多久猜對數字

min, max = 1, 100
ans = random.randint(min, max)
yourNum = int(input("請猜1~100間數字: "))
starttime = int(time.time())

while True:
    if yourNum == ans:
        print("恭喜答對")
        endtime = int(time.time())
        print("所花時間: ", endtime - starttime, "秒")
        break
    elif yourNum < ans:
        print("請猜大一些")
    else:
        print("請猜小一些")
    yourNum = int(input("請猜1~100間數字: "))

