#字串的替換:使用replace()

fn = '7月新番.txt'
with open(fn) as file_obj:
    data = file_obj.read()
    print('替換前:\n',data.rstrip())
    new_data = data.replace('魔術學姊', '擅長捉弄人的高木同學')   #替換字串
    print('替換後:\n', new_data.rstrip())
#注意原本的檔案內容並沒有改變,被替換掉的是data變數的值

#字串的尋找:使用find()
#回傳索引值 = 字串名稱.find(欲搜尋字串, start, end),找不到則傳回-1

with open(fn) as file_obj:
    obj_list = file_obj.readlines()

str_obj = ''

for line in obj_list:
    str_obj += line.rstrip()

findstr = input("請輸入欲搜尋字串: ")
index = str_obj.find(findstr)

if index != -1:
    print("%s在位置%d出現" % (findstr, index+1))
else:
    print("找不到!")
