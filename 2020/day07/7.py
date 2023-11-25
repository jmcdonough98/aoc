s = open('input.txt','r').read().split('\n')
from copy import copy

def parseInput():
    d = {}
    for l in s:
        k,v = l.split(" contain ")
        k = "".join(k.split(' ')[:2])
        tmp = [x.strip() for x in v[:-1].split(',')]
        vs = []
        for t in tmp:
            tmp2 = t.split(' ')
            try:
                vs.append((int(tmp2[0]),"".join(tmp2[1:3])))
            except:
                vs = None
        d[k] = vs
    return d

def p1(d):
    c = 0
    for bag in d.keys():
        c += bfs(bag,'shinygold',d)
    return c - 1

def bfs(n1,n2,d):
    visited = set()
    visited.add(n1)
    old = set()
    while visited != old:
        old = copy(visited)
        for v in old:
            if d[v] != None:
                visited.update([x[1] for x in d[v]])
    return n2 in old

def p2(n,d):
    c = 0
    if d[n] == None:
        return 0
    for bag in d[n]:
        tmp = p2(bag[1],d)
        c += bag[0]*(1 +p2(bag[1],d))
    return c

d = parseInput()
print(p1(d))
print(p2('shinygold',d))