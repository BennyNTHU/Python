#檔案的開啟讀取

fn = '國際歌.txt'       #欲開啟的檔案名稱,如果找不到會自動建立一個
file_obj = open(fn)     #用預設mode=r開啟檔案,傳回檔案物件file_obj
data = file_obj.read()  #讀取檔案內的資料到變數data
file_obj.close()        #關閉檔案,記得一定要關,否則可能會造成檔案內容損毀
print(data)             #輸出變數data

#我們也可利用with指令來開啟檔案,好處是指令結束後會自動關閉檔案

with open(fn) as file_obj:  #用預設mode=r開啟檔案,傳回檔案物件file_obj
    data = file_obj.read()
    print(data.rstrip())    #刪除末端字元

print('\n')

#利用for進行逐行讀取

with open(fn) as file_obj:
    for line in file_obj:   #組成txt檔案的基本單位可視為一行一行的文字
        print(line.rstrip())  #消除每行後的空白
print('\n')

#利用readlines()逐行讀取:此方法會將檔案的每一行(包含換行字元)儲存在一串列內
        
with open(fn) as file_obj:
    obj_list = file_obj.readlines() #每次只讀一行

print(obj_list)
print('\n')

#此時要怎麼組合成一篇文章呢?

str1 = '' #設定空字串
for line in obj_list:
    str1 += (line.rstrip() + '\n')

print(str1)
