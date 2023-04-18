c='aaab??!c!ls1kj'
a = list(set(c))
print(c)
for i in a:
    if not i.isalpha():
        a.remove(i)
print(a)
