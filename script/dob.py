#script to generate date of birth lists dd/mm/yyyy
#from year 1900 - 2030
file = open('dob.txt', 'w')
for years in range(1900, 2031):
    for e in range(1, 13):
        if e == 1 or e == 3 or e == 5 or e == 7 or e == 8 or e == 10 or e == 12:
            if e < 10:
                e1 = '0' + str(e)
                for l1 in range(1, 32):
                    if l1 < 10:
                        a1 = '0' + str(l1)
                        d11 = str(a1) + str(e1) + str(years)
                        file.write(f'{d11}\n')

                    else:
                        d1 = str(l1) + str(e1) + str(years)
                        file.write(f'{d1}\n')
            else:
                for l1e in range(1, 32):
                    if l1e < 10:
                        a1e = '0' + str(l1e)
                        d11e = str(a1e) + str(e) + str(years)
                        file.write(f'{d11e}\n')
                    else:
                        d1e = str(l1e) + str(e) + str(years)
                        file.write(f'{d1e}\n')  
        elif e == 2:
            e2 = '0' + str(e) 
            for l2 in range(1,30):
                if l2 < 10:
                    a2 = '0' + str(l2)
                    d22 = str(a2) + str(e2) + str(years)
                    file.write(f'{d22}\n')
                else:
                    d2 = str(l2) + str(e2) + str(years)
                    file.write(f'{d2}\n')
           
        elif e == 4 or e == 6 or e == 9 or e == 11:
            if e < 10:
                e3 = '0' + str(e)
                for l3 in range(1,31):
                    if l3 < 10:
                        a3 = '0' + str(l3)
                        d33 = str(a3) + str(e3) + str(years)
                        file.write(f'{d33}\n')
                    else:
                        d3 = str(l3) + str(e3) + str(years)
                        file.write(f'{d3}\n')
            else:
                for l3e in range(1, 31):
                    if l3e < 10:
                        a3e = '0' + str(l3e)
                        d33e = str(a3e) + str(e) + str(years)
                        file.write(f'{d33e}\n')
                    else:
                        d3e = str(l3e) + str(e) + str(years)
                        file.write(f'{d3e}\n')

file.close()
