str1 = 'I can\'t stop eating' #單引號作字串時裡面若有單引號要用溢出字元\'表示
str2 = "I can't stop eating" #雙引號作字串時不必理會單引號
str3 = " \"I can't stop eating\" "
print(str1)
print(str2)
print(str3)

str4 = "I can't \tstop \neating" #\t與\n為溢出字元，與C一樣代表tab跟換行
str5 = "I can't stop eating\b" #\b表刪除一個字元
str6 = "I can't stop eating\a" #響鈴
print(str4)
print(str5)
print(str6)

str7 = r"\'\aI can't\b \tst\"op \neating" #r代表使所有溢出字元失效
print(str7)
