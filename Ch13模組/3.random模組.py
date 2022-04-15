#random模組

import random

#randint()函數:語法為randint(min, max),產生介於min,max間的亂數
a = random.randint(1, 100)
print(a)

#choice()函數:在串列中隨機傳回一元素,參數為串列名稱
fruits = ['apple', 'banana', 'watermelon', 'peach']
print(fruits)
a = random.choice(fruits)
print(a)

#shuffle():將串列元素重新排列,參數為串列名稱
random.shuffle(fruits)
print(fruits)
