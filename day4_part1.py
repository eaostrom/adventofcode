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
        valid += 1
print(valid,'valid')
