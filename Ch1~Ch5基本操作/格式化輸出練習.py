score = 90
str1 = "Benny"
count = 1
formatstr = "%s's final score is %d"
print(formatstr % (str1, score))

x = 100
print("100的16進位 = %x\n100的8進位 = %o" % (x,x) )

x = 10
print("整數%d \n浮點數%f \n字串%s" % (x,x,x)) #會自動轉成不同的資料型態
y = 9.9
print("整數%d \n浮點數%f \n字串%s" % (y,y,y))

x = 100
print("x = /%6d/" %x) #表示總共用6位去顯示
y = 10.5
print("y = /%6.2f/" %y) #代表包含小數點共6位，小數點以下共n位數
s = "Deep"
print("s = /%6s/" % s)

print("以下為位數不夠用的例子")
print("x = /%2d/" % x) 
print("y = /%3.2f/" % y)
print("s = /%2s/" % s) #即使空間不夠，仍會完整輸出

print("以下為向左對齊的例子(預設向右)")
print("x = /%-6d/" % x)
print("y = /%-6.2f/" %y)
print("s = /%-6s/" % s)

print("顯示正號")
print("x = /%+6d/" % x) #正值資料會出現+號
print("y = /%+6.2f/" %y)

#.format的用法
print("{}的第{}次考試成績為{}" .format(str1, count, score))
