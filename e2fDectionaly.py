e2f = {
    "dog":"chien",
    "cat":"chat",
    "walrus":"morse",
}

# walrusを出力
print (e2f["walrus"])

# e2f convert f2e 
f2e = {}
for i, v in e2f.items():
    print (i, v)
    f2e[v] = i

print('output f2e')
print(f2e)

# call chien by f2e
print (f2e["chien"])
