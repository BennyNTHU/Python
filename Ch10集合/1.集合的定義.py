#集合
#利用大括號宣告集合,集合的元素是唯一的,如果有重複的元素會只顯示一個

int_set = {1, 2, 3, 4, 5}
my_wife = {'Nero', 'Jalter', 'Ishtar', 'Illiya', 'Ishtar'}  #有重複元素的集合

print(int_set)
print(my_wife)
print(type(int_set), type(my_wife))

#集合可以含不同的資料型態
#這個集合有整數,元組與字串的元素
mixed_set = {1, 2, (3, 4, 5), 'star burst stream'}
print(mixed_set)

#集合與字典都是由大括號定義,但{}卻是空字典
x = {}
print(x, type(x))

#如果我們想要定義空集合,或將其他資料型態轉成集合,可以使用set()函數
#字串,串列,元組可轉成字典
empty_set = set()   #建立空集合
print(empty_set, type(empty_set))

fruits = ['apple', 'banana', 'apple', 'orange', 'apple']
string = '棋子還是塞子, that is a question'
int_tuple = (1, 2, 3, 4)

print(fruits)
print(string)
print(int_tuple)

set_fruits = set(fruits)
set_string = set(string)
int_set = set(int_tuple)

print(set_fruits)
print(set_string)
print(int_set)

#運用set()函數可以將串列內重複的元素刪除
a = [1, 2, 2, 4, 5, 6, 32, 32, 5, 7, 8]
print("原本的a串列: ", a)
a = list(set(a))
print("後來的a串列: ", a)
