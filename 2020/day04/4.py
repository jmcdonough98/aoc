with open('input.txt','r') as f:
    passes = f.read().split('\n\n')

def parsePassport(_str):
    passport = {}
    tmp = _str.split('\n')
    for line in tmp:
        tmp2 = line.split(' ')
        for t in tmp2:
            k,v = t.split(':')
            passport[k] = v
    return passport
p1Valid = lambda p: len(p) == 8 or (len(p) == 7 and 'cid' not in p)

def checkRange(s,m,M):
    s = int(s)
    if s > M or s < m:
        return False
    return True

def p2Valid(p):
    if (not checkRange(p['byr'],1920,2002)):
        return False
    if (not checkRange(p['iyr'],2010,2020)):
        return False
    if (not checkRange(p['eyr'],2020,2030)):
        return False
    hgt = p['hgt']
    if hgt[-2:] in ['in','cm']:
        t = checkRange(hgt[:-2],150,193) if hgt[-2:] == 'cm' else checkRange(hgt[:-2],59,76)
        if not t:
            return False
    else:
        return False
    hcl = p['hcl']
    if hcl[0] != '#' or len(hcl) != 7:
        return False
    for c in hcl[1:]:
        if c not in "0123456789abcdef":
            return False
    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    pid = p['pid']
    if len(pid) != 9:
        return False
    for c in pid:
        if c not in "0123456789":
            return False
    return True
def day3():
    c = 0
    c2 = 0
    for k in passes:
        p = parsePassport(k)
        c += p1Valid(p)
        if p1Valid(p):
            c2 += p2Valid(p)
    return(c,c2)
print(day3())