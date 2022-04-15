#陣列元素的操作

#(一)append,pop,remove的用法
servent = ['Artoria','Emiya','Jalter','Nero','Capoo','Capoo']
print(servent)

servent.append('Ishtar')    #在串列尾端新增元素
print("課金之後的servent:",servent)

servent.insert(1, 'Osakabehime')    #在索引1位置"前方"插入新元素
print("再課一單,在索引1位置插入新角:",servent)

popped_servent = servent.pop()  #刪除最後一個元素
print("掛掉的servent是:", popped_servent)
print("剩下:", servent)

popped_servent = servent.pop(2) #刪除索引值為2的元素
print("又掛掉一隻servent:", popped_servent)
print("戰鬥結束,剩下:", servent)

servent.remove('Capoo') #刪除指定元素,但如果有重複,只會刪除第一個一次
print("有奇怪的東西混進來,被吃掉了:")
print("被吃掉後剩下的:",servent)

#(二) reverse, sort, sorted的用法
a = [2, 84, 13, 6, 10, 7, 35]
print("a = ", a)
a.reverse()   #顛倒陣列排序
print("顛倒順序後的a:", a)
print("再將a顛倒回來:", a[::-1])  #a[::-1]也可以達到顛倒的效果,但並不會更改a本身

a.sort()    #由小到大排序
print("a由小到大排序:", a)
a.sort(reverse = True)
print("a由大到小排序:", a)

a = [2, 84, 13, 6, 10, 7, 35]
print("目前串列a內容:", a)
a_sorted = sorted(a)    #不會更動a本身
print("使用sorted從小排到大:", a_sorted)
a_sorted = sorted(a, reverse = True)    #不會更動a本身
print("使用sorted從大排到小:", a_sorted)
print("原先串列a內容:", a)

#(三) index, count, join, extend的用法

servent = ['Artoria', 'Osakabehime', 'Emiya', 'Jalter', 'Nero', 'Nero', 'Artoria', 'Ishtar']
print("我的servent:", servent)

srh_str1 = 'Emiya'
srh_str2 = 'Nero'
i1 = servent.index(srh_str1) #取得指定元素的編號
i2 = servent.index(srh_str2)  #重複出現的元素,只會顯示第一次出現的索引值
print("%s是第 %d 號servent" % (srh_str1, i1))
print("%s是第 %d 號servent" % (srh_str1, i2))

num = servent.count(srh_str2)   #傳回指定元素內容出現的次數
print("我有 %d 隻%s" % (num, srh_str2))

char = '***'
print(char.join(servent))   #將串列個元素以char相連接
char = '\n'
print(char.join(servent))

servent = [['Jalter', 'Nero', 'Osakabehime'], 'Artoria', 'Emiya', 'Ishtar']
print("我的老婆們:", servent[0])
print("我老婆共有%d個" % (len(servent[0])) )
print("我超愛%s %s, 最近又抽到%s" % (servent[0][0], servent[0][1], servent[0][2]))


servent1 = ['Jalter', 'Nero', 'Osakabehime']
servent2 = ['Artoria', 'Emiya', 'Ishtar']
print("執行extend前")
print("servent1:", servent1)
print("servent2:", servent2)
servent1.extend(servent2)   #將串列servent2的各元素依序插入servent1後方
print("執行extend後")
print("servent1:", servent1)
print("servent2:", servent2)
