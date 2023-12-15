i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
g = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
a = input('>>')
result = ''
for e in a:
    if e in i or e.lower() in i:
        if e == e.upper():
            result += g[i.index(e.lower())].upper()
        else:
            result += g[i.index(e)]
    elif e in g or e.lower() in g:
        if e == e.upper():
            result += i[g.index(e.lower())].upper()
        else:
            result += i[g.index(e)]
    else:
        result += e
print(result)
