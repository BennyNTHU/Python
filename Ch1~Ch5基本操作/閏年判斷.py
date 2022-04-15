print("判斷輸入年份是否為閏年")
year = int(input("請輸入年分:"))

rem4 = year % 4
rem100 = year % 100
rem400 = year % 400

if rem4 == 0:
    if rem100 != 0 or rem400 == 0:
        print("%d 是閏年" % year)
    else:
        print("%d 不是閏年" % year)
else:
    print("%d 不是閏年" % year)
