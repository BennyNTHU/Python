#集合的基本函數操作

#max(), min(), sum():數值集合可取最大值與最小值,及算總和
#字串 字元集合可以依據unicode求最大值或最小值
num = {1, 2, 3, 4, 5}
print(max(num))
print(min(num))
print(sum(num))

ch = {'x', 'q', 'E', '>', 'a', 'R', 'x', '\n', '+'}
print(max(ch))
print(min(ch))

#len():列出集合元素的數量
print("集合ch元素個數: ", len(ch))

#sorted():會將集合轉為串列後排序,並將排序完的串列傳回
ch_sorted = sorted(ch)
ch_reverse = sorted(ch, reverse = True)
print("從小到大排列: ", ch_sorted)
print("從大到小排列: ", ch_reverse)

#enumerate物件與集合
drinks = {"coffee", "tea", "wine"}

enumerate_drinks = enumerate(drinks)    #打包為enumerate物件

print("enumerate_drinks的資料型態: ", type(enumerate_drinks))
print("將enumerate_drinks轉為串列輸出: ", list(enumerate_drinks))

for item in enumerate(drinks):
    print(item)

print('\n')
for count, item in enumerate(drinks):
    print(count, item)
    
print('\n')
for count, item in enumerate(drinks, 10):
    print(count, item)

