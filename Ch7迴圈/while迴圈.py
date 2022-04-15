#while 迴圈
#while迴圈執行的次數

i = 1
while i <= 5:
    print("第%d次while迴圈" % i)
    i += 1

#猜數字遊戲
answer = 30
guess = 0

while guess != answer:
    guess = int(input("請猜1到100間的數字 = "))
    if guess > answer:
        print("請猜小一點")
    elif guess < answer:
        print("請猜大一點")
    else:
        print("恭喜答對了")

#巢狀while迴圈列印99乘法表
    i = 1
    while i <= 9:
        j = 1;  #每次重設j
        while j <= 9:
            result = i * j
            print ("%d * %d = %-3d" % (i, j, result), end = " ")
            j += 1
        print() #換行
        i += 1

#利用break離開迴圈

a = [10, 11, 12, 13, 14, 15, 16]
n = int(input("請輸入輸出數"))
if n > len(a):
    n = len(a)
i = 0   #記得迴圈的索引值一定要先初始化
while i < len(a):
    if i == n:
        break
    print(a[i], end = " ")
    i += 1
print()

#利用continue暫時停止程式不往下執行
i = 0
while i <= 10:
    i += 1
    if (i % 2 != 0):
        continue    #i為奇數時就會跳過底下的敘述
    print(i)

#while迴圈與串列
anime = ['你遭難了嗎？',
'彼方的阿斯特拉',
'魔術學姐',
'騷亂時節的少女們',
'只要長得可愛，即使是變態你也喜歡嗎？',
'普通攻擊是全體二連擊，這樣的媽媽你喜歡嗎？',
'平凡職業造就世界最強',
'在地下城尋求邂逅是否搞錯了什麼第二季',
'科學一方通行']

notlonganime = []
longanime = []
verylonganime = []

while anime:    #對所有anime中的元素進行操作
    poped_anime = anime.pop()
    if len(poped_anime) >= 15:
        verylonganime.append(poped_anime)
    elif len(poped_anime) >= 10:
        longanime.append(poped_anime)
    else:
        notlonganime.append(poped_anime)
        
print("名子很長的動畫: ", verylonganime)
print("名子沒很長的動畫: ", longanime)
print("名子正常的動畫: ", notlonganime)

#while迴圈與enumerate
for a, count in enumerate(verylonganime, 10):
    print(count, a)

#pass的用法
#當迴圈中的程式還沒設計完畢時,可使用pass,但有時會造成無窮迴圈,要小心

schools = ['大葉大學', '真理大學', '佛光科大']
for school in schools:
    pass
