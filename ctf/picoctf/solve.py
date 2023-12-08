#combine = ord(flag[i]) << 8 + ord(flag[i+1])
# c = f + s
flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽'
num = []
for i in flag:
    tonum = ord(i) #combine or c
    removex256 = tonum >> 8 #this give ord(flag[i]) 
    getfirst = removex256 << 8 # turn into ord(flag[i]) << 8 or f
    getsecond = int(tonum) - int(getfirst) # this will get ord(flag[i+1]) or s
    turnintoletter = chr(removex256)
    turnsecondintoletter = chr(getsecond)
    num.append(turnintoletter)
    num.append(turnsecondintoletter)
    #print(f'getfirst {getfirst}')
    #print(f'removex256 {removex256}')
    #print(f'tonum {tonum}\n')

jointogether = ''.join(num)
print(jointogether)

