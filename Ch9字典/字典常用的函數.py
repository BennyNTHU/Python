#字典常用的函數

#len:取得字典個數
servant_data = {
    'Chole': {
        'Buster':1,
        'Art':2,
        'Quick':2
        },
    'Illiya':{
        'Buster':1,
        'Art':3,
        'Quick':1
        }
    }

print("servant_data字典元素個數 = ", len(servant_data))
print("servant_data['Chole']字典元素個數 = ", len(servant_data['Chole']))
print("servant_data['Illiya']字典元素個數 = ", len(servant_data['Illiya']))

#fromkeys()
#用來建立字典,首先我們需要一個串列或元組,當成字典的"鍵",然後指定值
#如果沒有指定值的話會用none當值

seq1 = ['name', 'city'] #利用串列設定key
list_dict1 = dict.fromkeys(seq1)    #沒有指定值
print("字典1 ", list_dict1)

list_dict2 = dict.fromkeys(seq1, 'Taipei')  
#只是這樣一來所有值都會是Taipei
#因為這個函數只能有兩個參數
#可以使用迴圈解決
print("字典2 ", list_dict2)

#get():搜尋字典的鍵並傳回值,如果找不到會傳回預設值
#語法:get(想搜尋的鍵,找不到時傳回的預設值)
fruits = {'Apple':20, 'Orange':25}

ret_value1 = fruits.get('Orange')
print("Value = ", ret_value1)

ret_value2 = fruits.get('Grape')
print("Value = ", ret_value2)

ret_value3 = fruits.get('Grape', 10)    #如果找不到傳回預設值10
print("Value = ", ret_value3)

#setdefault():跟get類似,用來搜尋字典的值並傳回
#但如果找不到時會把所搜尋的鍵加入字典中,其值為預設值

ret_value4 = fruits.setdefault('Orange')
print("Value = ", ret_value4)

ret_value5 = fruits.setdefault('Watermelon', 40)
print("Value = ", ret_value5)
print(fruits)

#pop():刪除字典元素,並傳回被刪除的元素的值
#找不到key時就傳回default,沒設定會回傳KeyError
ret_value6 = fruits.pop('Orange')
print("傳回刪除元素的值 = ", ret_value6)
print("刪除後的字典內容: ", fruits)

ret_value8 = fruits.pop('banana', 'DNE')    #預設值為'DNE'
print("傳回刪除元素的值 = ", ret_value8)
print("刪除後的字典內容: ", fruits)

ret_value7 = fruits.pop('banana')
print("傳回刪除元素的值 = ", ret_value7)    #程式會出現錯誤!
