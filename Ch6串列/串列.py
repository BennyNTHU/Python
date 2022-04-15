a = [10, 16, 87, 63, 9487]  #宣告串列
print("a陣列:", a)    #輸出a陣列
print("a陣列的資料型態", type(a))
print("a[1] = ", a[0])
print("a[2] = ", a[0])
print("a[3] = ", a[0])
print("a[4] = ", a[0])
print("a[5] = ", a[0])

b1, b2, b3, b4, b5 = a  #將a陣列的5個元素賦值給b1~b5五個整數
print(b1,b2,b3,b4,b5)

james = [23,19,22,31,18]    #宣告串列
print("James第1~第3場得分: ", james[0:3])    #Python會讀取james陣列中索引start=0到end-1=2的值
print("James第2~第4場得分: ", james[1:4])
print("James第1,3,5場得分: ", james[0:6:2]) #每隔step=2讀取james陣列中從索引start=0到索引end-1=5的值

warriors = ['Curry', 'Durant', 'Iquodala', 'Bell', 'Thompson']  #宣告串列
first3 = warriors[:3]   #串列前3個元素,即warriors[0]~warriors[2]
n_to_last = warriors[1:]    #warriors[1]到warriors[4]形成的串列
last3 = warriors[-3:]   #最後3個元素,即warriors[2]~warriors[4]
print("前三名球員", first3)
print("球員索引1到最後", n_to_last)
print("後3名球員", last3)
print("最後一位球員", warriors[-1])   #索引值-1代表最後一個元素
print("順序倒轉", warriors[-1], warriors[-2], warriors[-3],
                  warriors[-4], warriors[-5]) #索引-n號代表從後面數回來第n個元素

b = [4, 8, 7, 6, 3]
print("b串列的元素最大值 = ", max(b))   #陣列最大值
print("b串列的元素最小值 = ", min(b))   #陣列最小值
print("b串列的元素總和 = ", sum(b))    #陣列總和
print("b[2]~b[4]的元素總和 = ", max(b[2:5])) #從index為2讀到index為5-1=4
print("b[2]~b[4]的元素總和 = ", max(b[2:5]))
print("b[2]~b[4]的元素總和 = ", max(b[2:5]))
