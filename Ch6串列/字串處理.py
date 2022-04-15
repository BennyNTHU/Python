string = "I love Python"

#字串的索引與串列相同
print("string[0] = ", string[0])
print("string[5] = ", string[5])
print("string[7] = ", string[7])
print("string[8] = ", string[8])
print("string[-1] = ", string[-1])  #最後一個字元
print("string[-5] = ", string[-5])  #倒數第五個字元
print("string[-7] = ", string[-7])
print("string[-8] = ", string[-8])

#串列切片亦適用於字串
print("列印string索引0-4之元素 = '%s'" % string[0:5])
print("列印string索引1,3,5元素 = '%s'" % string[1:6:2])
print("列印string索引1到最後之元素 = '%s'" % string[1:])
print("列印string最後3個元素 = '%s'" % string[-3:])

print("字串長度", len(string))  #取得字串長度
#max,min函數應用在字串是看字元的unicode值
print("字串中有最大的unicode的字元:", max(string))
print("字串中有最小的unicode的字元:", min(string))    #空格

#會更動串列內容的方法或函數不能用在字串上
#因此要使用這些方法或函數需要先將字串改為串列型態
string2 = list('FatNerd')   #將字串改為串列型態
print(string2)
print(type(string2))

string2[3:] = 'Capoo'   #將字串改為串列後就可以更改內容了
print(string2)


#spilt的用法:
#spilt可以把字串以空格為為分隔符號,將字串拆開變成一個由"單字"組成的"字串串列"

slist = string.split()
print("串列內容:", slist)
print("串列字數:", len(slist))    #此時得到的是字串串列的長度(元素個數),即字數

#由於中文字之間沒有空格,因此spilt後只會有一個元素
chstring = "黑貞我老婆"
chlist = chstring.split()
print("中文串列內容:", chlist)
print("中文串列字數:", len(chlist))

