#part1

xfile = open('advent_day1.txt')
inp = xfile.read()
inp = inp.strip()

lines = inp.split('\n')
ints = []
for line in lines:
    ints.append(int(line))
for x in ints:
    y = 2020-x
    if y in ints:
        print(x,y)
