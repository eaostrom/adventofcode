import re
valid = 0
inp = open('input_day4.txt').read()
inp = inp.rstrip()
passport = inp.split('\n\n')
for items in passport:
    y= re.findall('[a-z]+:', items)

    if 'cid:' in y:
        y.remove('cid:')

    if len(y) == 7:
        byr = items.find('byr')+4
        year = int((items[byr:byr+4]))
        if 1920<=year<=2002:

            iyr = items.find('iyr')+4
            year = int((items[iyr:iyr+4]))
            if 2010<=year<=2020:

                eyr = items.find('eyr')+4
                year = int((items[eyr:eyr+4]))
                if 2020<=year<=2030:

                    hgt = re.findall('hgt:([0-9]+[a-z]+) ?', items)
                    for item in hgt:
                        if 'cm' in item:
                            try: cm = int(item[:3])
                            except: continue
                            if not 150<=cm<=193: continue
                        elif 'in' in item:
                            try: inch = int(item[:2])
                            except: continue
                            if not 59<=inch<=76: continue

                        hcl = re.findall('hcl:#([0-9a-f]+) ?', items)
                        if hcl == []: continue

                        ecl = ['amb','blu','brn','gry','grn','hzl','oth']
                        eyeclr = items.find('ecl')+4
                        color = items[eyeclr:eyeclr+3]
                        if color not in ecl: continue

                        pid = re.findall('pid:([0-9]+) ?', items)
                        if pid == []: continue
                        if len(pid[0]) == 9:
                            valid += 1

print(valid,'valid')
