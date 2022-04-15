#1個回傳值的函數
def subtract(x1, x2):
    return x1-x2

#很多回傳值的函數
def multi(x1, x2):
    add = x1 + x2
    sub = x1 - x2
    mul = x1 * x2
    div = x1 / x2
    return add, sub, mul, div

a = int(input())
b = int(input())
c = subtract(a, b)
print("%d - %d = %d" % (a, b, c))

add, sub, mul, div = multi(a, b)
print("%d + %d = %d" % (a, b, add))
print("%d - %d = %d" % (a, b, sub))
print("%d * %d = %d" % (a, b, mul))
print("%d / %d = %f" % (a, b, div))
