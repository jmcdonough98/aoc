import re
from functools import reduce

lines = open('input.txt','r').read().split('\n')

coords = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != "." and not lines[i][j].isdecimal():
            coords.append((i,j))

ids = []
for i in range(len(lines)):           
    for a in re.finditer(r"(\d+)", lines[i]):
        ids.append((int(a.group()), (i, a.span()[0]), (i, a.span()[1] - 1)))

count = 0
gears = {c:[] for c in coords}

for i in ids:
    for c in coords:
        if i[1][0] -1 <= c[0] <= i[1][0] + 1 and \
            i[1][1] - 1 <= c[1] <= i[2][1] + 1:
            count += i[0]
            gears[c].append(i[0])
            

print("Part 1:", count)
print("Part 2:", sum(reduce(lambda x,y: x*y, li ) for li in gears.values() if len(li) > 1))
