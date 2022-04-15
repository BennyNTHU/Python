#取得字典的資料:利用for+item()
#字典是一個無序的資料結構,Python只關注鍵-值配對而不關注元素順序
servants = {
    'Emiya': 'Archer',
    'Mash': 'Sheilder',
    'Artoria': 'Saber',
    'Osakabehime': 'Assassin',
    'Jalter': 'Avenger' }

for name, ser_class in servants.items():
    print("\n從者: ", name)
    print("職階: ", ser_class)

#如果只想要keys或value,可以這樣做
for name in servants.keys():
    print("\n從者: ", name)

for ser_class in servants.values():
    print("職階: ", ser_class)
    
#基本上字典是不能也不會去排序的,但在輸出結果時可以
for name in sorted(servants.keys()):
    print(name)

#字典串列
servant0 = {'name':'Emiya', 'class':'Archer', 'HP':80}
servant1 = {'name':'Mash', 'class':'Sheilder', 'HP':120}
servant2 = {'name':'Jalter', 'class':'Avenger', 'HP':76}
team = [servant0, servant1, servant2]
for servant in team:
    print(servant)

#利用for迴圈宣告字典串列
enemy = []

for i in range(50): #建立50個元素
    monster = {'name':'怪物', 'class':'Saber', 'HP':50}
    enemy.append(monster)

for monster in enemy[:3]:
    print(monster)

print("怪物數量 = ", len(enemy))

#字典元素內含串列
sports = {
    'Curry': ['籃球', '美式足球'],
    'Durant':['棒球'],
    'James':['美式足球', '棒球', '籃球'] }

for name, favorite_sport in sports.items():
    print("%s 喜歡的運動是: " % name)
    for sport in favorite_sport:
        print(sport)

#字典內含字典,此事字典是字典某個"鍵"的"值"
servant_data = {
    'Chole': {
        'Buster':1,
        'Art':2,
        'Quick':2
        },
    'Illiya':{
        'Buster':1,
        'Art':3,
        'Quick':1
        }
    }

for name, card in servant_data.items():
    print("從者名子: ", name)
    print("Buster卡數: ", card['Buster'])
    print("Art卡數: ", card['Art'])
    print("Quick卡數: ", card['Quick'])

#while迴圈在字典上的應用
survey_dict = {}    #建立空字典
flag = True    #判斷迴圈是否結束

while flag:
    name = input("請輸入姓名: ")
    travel_location = input("夢幻旅遊景點: ")

    survey_dict[name] = travel_location
    repeat = input("是否有人要參加市場調查?(y/n)")
    if repeat != 'y':
        flag = False

print("\n\n以下是市場調查結果")
for user, location in survey_dict.items():
    print(user, "夢幻旅遊景點: ", location)

#最後順便一提,Pythin跟VB一樣式強制你要縮排的程式語言,但只要縮排在同一層
#即使中間有空行都還能執行
    
