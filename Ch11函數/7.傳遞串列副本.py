#傳遞串列副本
def kitchen(unserved, served):
    print("處房處理顧客所點餐點")
    while unserved:
        current_meal = unserved.pop()
        print("菜單: ", current_meal)
        served.append(current_meal)

def show_unserved_meal(unserved):
    print("===下列是所點的餐點===")
    if not unserved:
        print("***沒有餐點***", "\n")
    for unserved_meal in unserved:
        print(unserved_meal)

def show_served_meal(served):
    print("===下列是已經服務的餐點===")
    if not served:
        print("***沒有餐點***", "\n")
    for served_meal in served:
        print(served_meal)

order_list = ['普羅旺斯鮮蚵青蔬佐滑蛋',
              '法式焗香奶油煎餅佐相思豆泥',
              '普羅旺斯嫩春雞佐地中海初榨橄欖油米蘭空運蘿勒葉']
served_list = []

show_unserved_meal(order_list)
show_served_meal(served_list)

kitchen(order_list[:], served_list)    #這時是傳遞order_list的副本
print("\n", "===廚房處理結束===", "\n")

show_unserved_meal(order_list)  #仍然沒變
show_served_meal(served_list)
