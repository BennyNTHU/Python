#寫入檔案
'''
開啟檔案的各種mode: open(檔案名稱,模式)
'r':預設模式,唯讀,只能讀取
'w':可以寫入檔案,如果重複寫入會把檔案內容全部洗掉後,再寫入新的
'r+':可以讀取與寫入
'a':可以寫入檔案,重複寫入時會把新的內容加在原有內容的後面
'''
#寫入檔案的方法:檔案物件.write(輸出資料)
#write()只能寫入字串!而且不會在字串後自動換行

fn = '書單.txt'
str1 = '電磁學'
str2 = '通訊系統'

with open(fn, 'w') as file_obj: #以寫入模式打開檔案
    file_obj.write(str1 + '\n')      #寫入資料
    file_obj.write(str2 + '\n')

with open(fn, 'a') as file_obj: #以寫入模式打開檔案
    file_obj.write('微分幾何' + '\n')
    
