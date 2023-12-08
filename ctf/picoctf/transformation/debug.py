i = 0
flag = 'worlds'
while i < len(flag):
    first = ord(flag[i]) << 8
    second = ord(flag[i + 1])
    uni = first + second
    combine_letter = chr(first + second)
    before_multi = ord(flag[i])
    which_letter = flag[i]
    number_beforeplusone = ord(flag[i])
    removex256 = uni >> 8
    firstbinary = '{0:08b}'.format(int(first))
    letterofsecond = chr(second)
    secondbinary = '{0:08b}'.format(int(second))
    binarycombine = '{0:08b}'.format(int(uni))
    combinebinaryafterremove256 = '{0:08b}'.format(int(removex256))
    beforex256binary = '{0:08b}'.format(int(before_multi))
    print(f'on number: {i}, on letter: {which_letter},\nbefore x256: {before_multi}, after x256/first: {first},remove x256: {removex256},\nnbpo: {number_beforeplusone},letter of second: {letterofsecond}, second: {second},\nunicode after combine: {uni}, letter after combine: {combine_letter},\nfirst binary: {firstbinary}, second binary: {secondbinary}, binary combine: {binarycombine}, before remove binary: {beforex256binary}, binary after remove x256: {combinebinaryafterremove256} \n\n',)
    i += 2
