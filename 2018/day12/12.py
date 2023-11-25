def parseInput(path):
    f = open(path,'r').read().splitlines()
    pots = f[0].split("state: ")[1]
    rules = []
    for i in range(2,len(f)):
        tmp = f[i].split(" => ")
        rules.append((tmp[0],tmp[1]))
    return pots,rules
def simulateGeneration(pots,rules):
    needPadding = False
    changes = []
    for i,p in enumerate(pots):
        try:
            adj = pots[i-2:i+2+1]
        except IndexError:
            continue
        for r in rules:
            if adj == r[0]:
                changes.append((i,r[1]))
                break
    pots = list("."*(len(pots)))
    for c in changes:
        pots[c[0]] = c[1]
    if pots[-5:].count("#") > 0:
        needPadding = True
    pots = "".join(pots)
    if needPadding:
        pots += padding
    return pots
def plantSum(pots,lIndex):
    s = 0
    for i in range(len(pots)):
        if pots[i] == "#":
            s += (i + lIndex)
    return s
padSize = 30
padding = "."*padSize

pots,rules =  parseInput("input.txt")
pots = padding + pots + padding
lIndex = 0 - padSize
for i in range(10000):
    if i % 1000 == 0:
        print plantSum(pots,lIndex), i*50 + 695 #it just werks lmao
    pots = simulateGeneration(pots,rules)
    newIndex = pots.index("#") - 5 
    if newIndex > 0:
        lIndex += newIndex
        pots = pots[newIndex:]
#Experimentally determine a formula, 
# the 50 plants shift down by exactly 1000 after 1000 iterations, so the solution should be:
print 50000000000*50 + 695
