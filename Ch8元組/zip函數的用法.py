#zip()函數:會將iterable的物件(如串列等)打包成tuple再傳給zip物件
title = ['Name', 'Age', 'Hometown', 'class']
info = ['Nero Claudius', '28', 'Roma', 'Saber']

zipData = zip(title, info)  #將兩個list打包

print(type(zipData))    
print(zipData)  #會輸出記憶體位置

servant = list(zipData) #轉為list輸出,這個list的元素是tuple
print(servant)

#如果兩串列元素不相等,只會就輸出較短的串列打包
info2 = ['Emiya', 30]
zipData2 = zip(title, info2)

servant2 = list(zipData2)
print(servant2)

#利用*可以把zip解開,恢復串列
t, i = zip(*servant)    #執行unzip的對象是轉為串列後的資料
print("title = ", t)
print("info = ", i)
