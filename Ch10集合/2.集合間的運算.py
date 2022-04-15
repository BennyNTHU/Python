#交集"&", 聯集"|", 差集"-"

kevin = {'電磁學', '訊號與系統', '近代物理', '機率', '國防'}
peter = {'訊號與系統', '微處理機', '嵌入式', '機率'}

k_and_p = kevin & peter
print("兩人都被當的科目: ", k_and_p)

k_or_p = kevin | peter
print("兩人被當的所有科目: ", k_or_p)

k_p = kevin - peter
print("Kevin被當但peter沒被當的科目: ", k_p)

p_k = peter - kevin
print("peter被當但kevin沒被當的科目: ", p_k)

#對稱差集"^": A|B-A&B
k_sydi_p = kevin ^ peter
print("兩人沒有一起被當的科目: ", k_sydi_p)

#以上的運算也可以藉由一些函數完成
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

AandB = A.intersection(B)
BandA = B.intersection(A)

AorB = A.union(B)
BorA = B.union(A)

A_B = A.difference(B)
B_A = B.difference(A)

A_sydi_B = A.symmetric_difference(B)
B_sydi_A = B.symmetric_difference(A)

print("A跟B的交集: ", AandB)
print("B跟A的交集: ", BandA)
print("A跟B的聯集: ", AorB)
print("B跟A的聯集: ", BorA)
print("A跟B的差集: ", A_B)
print("B跟A的差集: ", B_A)
print("A跟B的對稱差集: ", A_sydi_B)
print("A跟B的對稱差集: ", B_sydi_A)

#判斷兩集合是否相等,若相等則回傳True, 不相等回傳False
C = {1, 2, 3, 4, 5}
print("A與C相等? ", A == C)
print("A與B相等? ", A == B)

#判斷兩集合是否不相等, 不相等回傳True, 相等回傳False
print("A與C不相等? ", A != C)
print("A與B不相等? ", A != B)

#判斷一元素是否屬於集合
flag = 1 in A
flag2 = 1 in B
print("1是否在A中? ", flag)
print("1是否在B中? ", flag)

#判斷一元素是否不屬於集合
flag = 1 not in A
flag1 = 1 not in B
print("1是否不在A中? ", flag)
print("1是否不在B中? ", flag1)
