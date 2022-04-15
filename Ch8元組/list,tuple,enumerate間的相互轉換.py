#資料型態間的轉換
#串列,元組和enumerate間可以互換

#元組改為串列
anime = ('你遭難了嗎？','彼方的阿斯特拉','魔術學姐','流汗吧!健身少女')
list_anime = list(anime)
print("列印元組", anime, "資料型態 = ", type(anime))
print("列印串列", list_anime, "資料型態 = ", type(list_anime))

#改為串列後就能對元素進行操作
list_anime[0] = '科學一方通行'
list_anime.pop()
list_anime.append('擅長捉弄人的高木同學S2')
print("修改後的動畫清單: ", list_anime)

#串列改為元組
tuple_anime = tuple(list_anime)
print("修改後的動畫清單: ", tuple_anime)
#tuple_anime.pop()    #會出現錯誤

#元組改為anime
enumerate_anime = enumerate(tuple_anime)
print("轉成元組輸出,初始值是0: ", tuple_anime)
enumerate_anime = enumerate(tuple_anime, start = 5)
print("轉成元組輸出,初始值是5: ", tuple_anime)
