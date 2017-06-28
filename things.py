things = ["mozzarella", "cinderella", "salmonella"]

# リストの中身は書き換えない
tmp = things[1].capitalize()
print (tmp)

# 人間の要素の先頭文字を大文字に
things[1] = "Cinderella"
print (things)

# チーズの種類を大文字に
things[0] = things[0].upper()
print (things)

# 病気のものを削除
del things[2]
print (things)
