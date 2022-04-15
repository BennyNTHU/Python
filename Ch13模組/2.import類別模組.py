#導入類別模組

from banks import Banks, Shilin_Banks   #導入banks中的兩個類別

jamesbank = Banks('James')
print("James banks = ", jamesbank.bank_title())
jamesbank.save_money(500)
jamesbank.get_balance()

hungbank = Shilin_Banks('Hung')
print("Hung's banks = ", hungbank.bank_title()) 

#要導入所有類別,可以用
from banks import *

#如果寫成
import banks

#那就要用"."來引用模組中的各個類別
hungbank = banks.Shilin_Banks('Hung')
print("Hung's banks = ", hungbank.bank_title()) 
