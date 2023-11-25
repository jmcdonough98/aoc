import regex as re
s = open('input2.txt','r').read()

rules, _input = s.split('\n\n')

def parseRules(rules):
    ruleMap = {}
    for line in rules.split('\n'):
        tmp = line.split(': ')
        ruleno, vals = tmp[0],tmp[1]
        ruleno = int(ruleno)
        try:
            tmp = vals.split(' | ')
            ruleMap[ruleno] = []
            for t in tmp:
                ruleMap[ruleno].append([int(x) for x in t.split(' ')])
        except:
            ruleMap[ruleno] = tmp[0][1]
    return ruleMap

exprs = {}

def makeExpr(n,ruleMap,p2=False):
    if n in [8,11] and p2:
        if n == 11:
            exprs[n] =  makeExpr(42,ruleMap,p2)  + '(?R)?' + makeExpr(31,ruleMap,p2)
            return exprs[n]
        elif n == 8:
            exprs[n] = '(' + makeExpr(42,ruleMap,p2) + ")+"
            return exprs[n]
    if n in exprs:
        return exprs[n]
    if ruleMap[n] in ['a','b']:
        return ruleMap[n]
    s = '('
    s +=  "".join([makeExpr(n2,ruleMap,p2) for n2 in ruleMap[n][0]])
    try:
        tmp = ')|(' + "".join([makeExpr(n2,ruleMap,p2) for n2 in ruleMap[n][1]]) 
    except: #no '|' in rule
        exprs[n] = s + ')'
        return exprs[n]
    exprs[n] = '(' + s + tmp + '))'
    return exprs[n]

def day19(_input,ruleMap):
    ruleMap = parseRules(rules)
    ex = makeExpr(0,ruleMap,True)
    ex1 = '^(' + exprs[42] + ')+'
    ex2 = '(' + exprs[31] + ')+$'
    ex = ex1+ex2
    c2 = 0
    print(ex)
    for l in _input.split('\n'):
        if re.match(ex,l) != None:
            len1 = len(l)
            l = re.sub(ex1,'',l)
            if len1 - len(l) > len(l):
                c2 += 1

    return c2
ruleMap = parseRules(rules)
print(day19(_input,ruleMap))