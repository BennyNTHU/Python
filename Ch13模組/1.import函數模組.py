#利用import引進模組,並利用"模組名稱.函數名稱"呼叫函數
import makefood

makefood.make_icecream('草莓醬')
makefood.make_icecream('豆腐', '麻油雞', '醬油')
makefood.make_drink('large', 'coke')

                    
#只想導入模組內單一函數,可以用以下語法,且此時就不用使用"."了
from makefood import make_icecream
make_icecream('草莓醬')

#如果想導入多個函數,用","隔開,一樣不用使用"."
from makefood import make_icecream, make_drink

#導入所有函數,一樣不用使用"."
from makefood import *

'''可以給模組內的函數在所設計的程式內,利用"as"給一個替代名稱
通常會這麼做的原因是因為程式裡面有相同名稱的函數,
或模組內的函數名子太長'''
from makefood import make_icecream as ice
ice('苦瓜')

#模組也可以有替代名稱
import makefood as m
m.make_drink('Extra large', '肥宅快樂水')

#這個程式只是範例,所有import建議寫在程式最頂端
