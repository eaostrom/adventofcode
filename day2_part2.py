valid=0
fh = open('input_day2.txt')
for line in fh:
    count=0
    line=line.rstrip()
    col = line.find(':')
    pw = line[col+1:]
    letter = line[col-1]

    hyp = line.find('-')
    pos_1 = int(line[:hyp])
    pos_2 = int(line[hyp+1: col-2])

    if pw[pos_1] == letter and pw[pos_2] != letter:
        valid= valid+1
    elif pw[pos_1] != letter and pw[pos_2] == letter:
        valid= valid+1
print(valid)
