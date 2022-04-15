clastname = input("請輸入中文姓氏:")
cfirstname = input("請輸入中文名字:")
cfullname = clastname + cfirstname
print("%s 歡迎使用本系統" % cfullname)

lastname = input("請輸入英文姓氏:")
firstname = input("請輸入英文名子:")
fullname = firstname + " " + lastname
print("%s Welcome to SSE system" % fullname)

print("歡迎使用成績輸入系統")
engh = input("請輸入英文成績:")
math = input("請輸入數學成績")
total = int(engh) + int(math)
print("name資料型別是",type(name))
print("engh資料類型是",type(engh))
print("%s / %s 你的總分是 %d" % (cfullname, fullname, total))
