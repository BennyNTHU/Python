#類別
'''
Python作為物件導向的程式語言,當然也有類別的功能
Python的類別由"屬性"與"方法"組成,對應C++類別中中的"資料成員"與"函數成員"
'''

class Banks():              #定義Banks類別
    title = 'Taipei Bank'   #定義屬性
    def motto(self):        #定義方法,只有Banks類別能呼叫此方法
                            #self是一定要加的參數,是為了Python編譯用,呼叫時不需傳遞此參數
        return "以客為尊"

userbank = Banks()          #定義Banks類別物件userbank
print(userbank.title)       #呼叫類別屬性
print(userbank.motto())     #呼叫類別方法
