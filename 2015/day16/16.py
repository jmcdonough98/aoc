from collections import defaultdict
with open('input.txt','r') as f:
    lines = f.read().split('\n')

def parseGranny(l):
    tmp = l[l.find(":")+2:].split(', ')
    g = defaultdict(int)
    for t in tmp:
        a,b = t.split(": ")
        g[a] = int(b)
    return g
GRANNY = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}
def checkGrannyP1(g):
    flag = True
    for thing in g.keys():
        if GRANNY[thing] != g[thing]:
            return False
    return True
    # return False
def checkGrannyP2(g):
    flag = True
    ge = ['cats','trees']
    le = ['pomeranians','goldfish']
    for thing in g.keys():
        if thing in ge and g[thing] <= GRANNY[thing]:
            return False
        if thing in le and g[thing] >= GRANNY[thing]:
            return False
        if thing not in le and thing not in ge and g[thing] != GRANNY[thing]:
            return False
    return True
for i,l in enumerate(lines):
    g = parseGranny(l) 
    if checkGrannyP1(g):
        print('PART 1:', i+1)
    if checkGrannyP2(g):
        print('PART 2:', i+1)