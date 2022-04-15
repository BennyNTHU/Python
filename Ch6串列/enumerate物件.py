#enumerate物件:一種將索引值與元素配對的方式組成的資料結構
#這些元素可以來自串列,元組或集合

drinks = ["coffee", "tea", "wine"]  #先宣告一陣列
print("drinks的資料型態:", type(drinks))
print(drinks)

enu_drinks = enumerate(drinks)  #將串列轉為enumerate資料結構
print("enu_drinks的資料型態", type(enu_drinks))
print(enu_drinks)   #輸出一enumerate物件,會得到其記憶體位址!

#若想獲得enumerate資料結構中的內容,需將其轉回list
print("轉換成串列輸出, 初始值是0 = ", list(enu_drinks))

#將串列轉為enumerate資料結構,預設索引值是由0開始
#但也可以從其他數字開始
enu_drinks = enumerate(drinks, start = 10)  #索引值由10開始
print("轉換成串列輸出, 初始值是10 = ", list(enu_drinks))
