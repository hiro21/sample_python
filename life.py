life = {
        'animals':{'cats':['Henri','Grumpy','Lucy'], 'octopi':'', 'emus':''},
        'plants':{},
        'other':{},
        }

print (life)

mostOnKeys = set(life)
print (mostOnKeys)

# animalsのキー
for i, k in life:
    print (k)
