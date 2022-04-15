#參數預設值:在參數列利用等號可以設定參數預設值

def build_vip(id, name = 'vip', tel = ''):  #tel的預設值是空字元, name的預設值是vip
    vip_dict = {'VIP_ID':id, 'Name':name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict

while True:
    print("建立VIP資訊系統")
    idnum = input("請輸入ID: ")
    name = input("請輸入姓名: ")     #如果這行直接按Enter,相當於輸入了換行字元,因此預設值不會起作用
    tel = input("請輸入電話號碼: ")    #如果這行直接按Enter,將不會建立此欄位
    member = build_vip(idnum, name, tel)
    print(member)
    
    repeat = input("是否繼續(y/n)")
    if repeat != 'y':
        break

