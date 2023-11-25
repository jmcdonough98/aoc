from collections import defaultdict
lines = open('input.txt','r').read().split('\n')
coords = []
for l in lines:
    a,b = l.split(' -> ')
    x0,y0 = [int(x) for x in a.split(',')]
    x1,y1 = [int(x) for x in b.split(',')]
    coords.append([[x0,y0],[x1,y1]])
points = defaultdict(int)

for c in coords:
    if c[0][0] == c[1][0]:
        m1 = min(c[0][1],c[1][1])
        m2 = max(c[0][1],c[1][1])
        for i in range(m1,m2 + 1):
            points[(c[0][0],i)] += 1
    elif c[0][1] == c[1][1]:
        m1 = min(c[0][0],c[1][0])
        m2 = max(c[0][0],c[1][0])
        for i in range(m1,m2 + 1):
            points[(i,c[0][1])] += 1
    else:
        mx1 = min(c[0][0], c[1][0])
        mx2 = max(c[0][0], c[1][0])
        my1 = min(c[0][1], c[1][1])
        my2 = max(c[0][1] ,c[1][1])
        if (c[0][0] < c[1][0] and c[0][1] < c[1][1]) or \
            (c[0][0] > c[1][0] and c[0][1] > c[1][1]):
            for i in range(mx2 - mx1 + 1):
                points[mx1 + i, my1 + i] += 1
        else:
            for i in range(mx2 - mx1 +1):
                points[mx2 - i, my1 + i] += 1
            pass
count = 0
for p in points:
    if points[p] > 1:
        count += 1
print(count)