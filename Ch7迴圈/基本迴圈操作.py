#for迴圈實作

players = ['curry', 'jordan', 'james', 'durant', 'obama']

for player in players:   #for變數in物件,該變數不必先宣告
    print(player)

for player in players: print(player)    #也可以這樣寫

#迴圈內有多行敘述時
for player in players:
    print(player.title() + ", it was a great game") #將首字轉為大寫
    print("加薪500塊" + player.title())

#當只想修改某些元素時

print("前3位球員:")
for player in players[:3]:   #取得串列前三個元素
    print(player)

print("後三位球員")
for player in players[-3:]:  #取得串列後三個元素
    print(player)

#range函數:range(n)用來產生整數串列,比如:
n = 5
a = list(range(n))
print(type(a))
print(type(range(n)))   #資料型態是range
print(range(n)) #輸出:range(0, 5)
print("當n = %d時, list(range(n)) = " % n, a)

#range函數可拿來操作迴圈
start = -5
end = 3
for number in range(start, end):
      print(number) #這樣輸出會換行

step = 3    
for number in range(start, end, step):  #代表以3為公差輸出一次,step也可以是負數
      print(number)

