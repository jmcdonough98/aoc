s = open('input.txt','r').read().split('\n\n')

def isValid(tick,con):
    for val in tick:
        valid = False
        for c in con:
            if c[0][0] <= val <= c[0][1] or c[1][0] <= val <= c[1][1]:
                valid = True
                break
        if not valid:
            return val

singleCon = lambda x, c: c[0][0] <= x <= c[0][1] or c[1][0] <= x <= c[1][1]
def checkCol(con, validTickets,i):
    for tick in validTickets:
        if not singleCon(tick[i], con):
            return False
    return True

def determineMapping(constraints,validTickets):
    mapping = {}
    for k in range(len(constraints)):
        mapping[k] = []
        for i in range(len(validTickets[0])):
            if checkCol(constraints[k],validTickets,i):
                mapping[k].append(i) 
    tmap = {}      
    # sort of back substitution lol
    for k in sorted(mapping.keys(), key = lambda x: len(mapping[x])):
        tmp = mapping[k][0]
        tmap[k] = tmp
        for k2 in mapping.keys():
            try:
                mapping[k2].remove(tmp)
            except:
                continue
    return tmap

lines = s[0].split('\n')
constraints = []
for line in lines:
    tmp = line.split(': ')
    r1,r2 = tmp[1].split(' or ')
    r1 = r1.split('-')
    r2 = r2.split('-')
    constraints.append(((int(r1[0]),int(r1[1])),(int(r2[0]),int(r2[1]))))

counter = 0
tmp = s[2].split(':')[1].split('\n')
validTickets = []
for l in tmp[1:]:
    try:
        x = [int(y) for y in l.split(',')]
        tmp =isValid(x,constraints)
        if tmp != None:
            counter += tmp
        else:
            validTickets.append(x)
    except:
        continue


tmap = determineMapping(constraints,validTickets)
myTicket = [113,53,97,59,139,73,89,109,67,71,79,127,149,107,137,83,131,101,61,103]
ans = 1
for i in range(6):
    ans *= myTicket[tmap[i]]
print(counter, ans)
