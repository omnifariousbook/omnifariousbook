import hashlib 
username_trial = b"FRASER"
firstpart = "picoCTF{1n_7h3_|<3y_of_"
thirdpart = "}"
i = [hashlib.sha256(username_trial).hexdigest()[4],
     hashlib.sha256(username_trial).hexdigest()[5],
     hashlib.sha256(username_trial).hexdigest()[3],
     hashlib.sha256(username_trial).hexdigest()[6],
     hashlib.sha256(username_trial).hexdigest()[2],
     hashlib.sha256(username_trial).hexdigest()[7],
     hashlib.sha256(username_trial).hexdigest()[1],
     hashlib.sha256(username_trial).hexdigest()[8]
     ]
o = ''
for l in i:
    o += l
print(firstpart + o + thirdpart)
