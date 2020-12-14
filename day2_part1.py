valid=0
fh = open('input.txt')
for line in fh:
    count=0
    line=line.rstrip()
    col = line.find(':')
    pw = line[col+2:]

    letter = line[col-1]
    for l in pw:
        if l == letter:
            count = count+1

    hyp = line.find('-')
    min = int(line[:hyp])
    max = int(line[hyp+1: col-2])

    if min<=count<=max:
        valid= valid+1
print(valid)
