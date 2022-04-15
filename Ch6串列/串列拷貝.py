#Deep copy實作:Deep copy是指一串列賦值給另一串列後
#若更動其中之一,則另一串列也跟著被更動的情形
#這是由於兩個串列的變數位址相同

print("Deep Copy")

mysports = ['basketball', 'baseball']
friendsports = mysports     #deep copy

print("列出mysports位址 = ", id(mysports))  #取得變數位址
print("列出friendsports位址 = ", id(friendsports))

print("我喜歡的運動:", mysports)
print("我朋友喜歡的運動:", friendsports)

mysports.append('football') #經由此操作,兩串列都會增加'football'
friendsports.append('soccer')   ##經由此操作,兩串列都會增加'soccer'

print("新增項目後")

print("列出mysports位址 = ", id(mysports))  #取得變數位址
print("列出friendsports位址 = ", id(friendsports))

print("我喜歡的最新運動:", mysports)
print("我朋友喜歡的最新運動:", friendsports)
print('\n')


#shallow copy:如同C或C++的陣列一般,將被賦值得陣列存在不同位址

print("shallow Copy")

mysports = ['basketball', 'baseball']
friendsports = mysports[:]     #shallow copy

print("列出mysports位址 = ", id(mysports))  #取得變數位址
print("列出friendsports位址 = ", id(friendsports))

print("我喜歡的運動:", mysports)
print("我朋友喜歡的運動:", friendsports)

mysports.append('football') #經由此操作,只有mysports串列會增加'football'
friendsports.append('soccer')   ##經由此操作,只有friendsports串列會增加'soccer'

print("新增項目後")

print("列出mysports位址 = ", id(mysports))  #取得變數位址
print("列出friendsports位址 = ", id(friendsports))

print("我喜歡的最新運動:", mysports)
print("我朋友喜歡的最新運動:", friendsports)
print('\n')
