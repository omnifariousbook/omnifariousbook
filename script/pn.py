file = open('pn.txt', 'w')
pn = ['012', '085', '092', '077']
for i in pn:
    for e in range(100000, 1000000):
        d = i + str(e)
        file.write(f'{d}\n')
