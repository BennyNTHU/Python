#凍結集合:內容無法更改,但可以求交集,聯集等等不牽涉元素更動的方法

X = frozenset([1,3,5])
Y = frozenset([5,7,9])
print(X)
print(Y)

print("X與Y的交集", X & Y)
print("X與Y的聯集", X | Y)

A = X & Y   #兩凍結集合做運算後仍為凍結集合
print(A)

Z = {3, 5, 6}   
print(X & Z)    #凍結集合與一般集合運算,會變成凍結集合
