#sys模組與keyword模組

import sys
import keyword

#version屬性:sys模組中可列出目前Python的版本訊息
print("目前Python版本是: ", sys.version)

#stdin物件:屬於sys模組,
#搭配readline方法,可讀取螢幕輸入直到按下鍵盤上Enter的字串
#參數為要讀進去的字元數
print("請輸入字串,輸入完按enter: ", end = "")
msg = sys.stdin.readline(8)
print(msg)

#stdout物件:屬於sys模組,搭配write()方法,從螢幕輸出資料
sys.stdout.write("刑部姬大好\n")

#kwlist屬性:keyword模組中含有所有Python關鍵字的屬性
print(keyword.kwlist, '\n')

#iskeyword():傳回參數的字串是否含有關鍵字
keywordlist = ['for', 'a', 'in', 'intlist', ':']
for x in keywordlist:
    print("%8s " %x, keyword.iskeyword(x))
