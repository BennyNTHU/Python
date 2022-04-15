#is與not is 的練習

x = 10
y = 10
z = 15
r = z - 5

#物件1 is 物件2 用來判斷兩物件是否有相同的記憶體位置
#在Python中有相同值的物件會被放在同一個記憶體位置中

bool_value = x is y     #此傳回值的資料型態是布林值
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d" % (x, y), bool_value)

bool_value = x is z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d" % (x, z), bool_value)

bool_value = x is r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d" % (x, r), bool_value)

bool_value = x is not y
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d" % (x, z), bool_value)

bool_value = x is not z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d" % (x, z), bool_value)

bool_value = x is not r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d" % (x, r), bool_value)
