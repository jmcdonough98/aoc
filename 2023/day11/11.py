def getDists(s, scale, eRows, eCols):
    pts = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == "#":
                pts.append((i,j))
    d = 0
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            p = pts[i]
            q = pts[j]
            rc = len([x for x in eRows if min(p[0],q[0]) <= x <= max(p[0], q[0])])
            cc = len([x for x in eCols if min(p[1],q[1]) <= x <= max(p[1], q[1])] )
            d += abs(p[0] - q[0]) + abs(p[1] - q[1]) + (scale - 1)*(rc + cc)
    return d 


if __name__ == "__main__":
    s = open('input.txt','r').read().split('\n')
    emptyRows = []
    for i,l in enumerate(s):
        if l == '.'*len(s[0]):
            emptyRows.append(i)
    emptyCols = []
    for j in range(len(s[0])):
        if "".join(x[j] for x in s) == "."*len(s):
            emptyCols.append(j)

    print("Part 1:", getDists(s, 2, emptyRows, emptyCols))
    print("Part 2:", getDists(s, 1000000, emptyRows, emptyCols))
