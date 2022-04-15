#break的用法
#break用來跳出所屬的迴圈

for digit in range(1, 11):
    if digit == 5:
        break;  #離開for迴圈
    print(digit, end = ', ')

print('\n')

for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end = ', ')

a = ['a','b','c','d','e','f','g','h']
n = int(input("\n請輸入輸出數 = "))
if n > len(a):
    n = len(a)
i = 0
for ch in a:
    if i == n:  #只輸出n筆資料
        break
    print(ch, end=' ')
    i += 1

#continue的用法
#continue會用來跳過continue以下的迴圈敘述
a = [32, 54, 87, 21, 6, 51, 21, 32]
i = 0
for num in a:
    if num < 50:
        continue
    i += 1
print("\n有%d個數>50" % i)

#for-else迴圈
#else是for迴圈最後一次執行時會執行的區域
num = int(input("請輸入>1的整數做質數測試"))
if num == 2:
    print("%d是質數" % num)
else:   #這個else是歸if管
    for n in range(2, num):
        if num % n == 0:
            print("%d不是質數" % num)
            break
    else:   #這個else是for執行到最後一圈的時要做的
        print("%d是質數" % num)
