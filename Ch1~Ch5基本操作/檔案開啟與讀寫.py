fstream1 = open("d:\out1.txt", mode = "w")  #會複寫已存在的資料
print("Test for output", file = fstream1)
fstream1.close()

fstream2 = open("d:\out2.txt", mode = "a")  #"a"表新寫入的資料會附在後面
print("Testing for output", file = fstream2)
fstream2.close()
