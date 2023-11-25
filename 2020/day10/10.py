s = sorted([int(x) for x in open('input.txt','r').read().split('\n')])
from itertools import groupby

tmp = [s[i] - s[i-1] for i in range(1,len(s))]
runs = [len(list(x[1])) for x in groupby(tmp) if x[0] == 1]
runs[0] += 1 #can't forget about 0 :)
p2c = 1
for v in runs:
    if v == 4:
        p2c *= 7
    elif v == 3:
        p2c *= 4
    elif v == 2:
        p2c *= 2
print((tmp.count(3)+1) * (tmp.count(1)+1))
print(p2c)

    