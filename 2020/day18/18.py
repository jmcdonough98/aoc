import operator as op
s = open('input.txt','r').read().split('\n')

def evaluateExpression(s):
    valStack = [0]
    opStack = [op.add]
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == '(':
            valStack.append(0)
            opStack.append(op.add)
        elif ch == ')':
            opStack.pop()
            tmp = valStack.pop()
            valStack[-1] = opStack[-1](valStack[-1],tmp)
        elif ch == '+':
            opStack[-1] = op.add
        elif ch == '*':
            opStack[-1] = op.mul
        elif ch == ' ':
            pass
        else:
            valStack[-1] = opStack[-1](valStack[-1],int(ch))
        i += 1
    return valStack[0]

def addParens(s):
    newS = "(("
    for c in s:
        if c == '(':
            newS += '((('
        elif c == ')':
            newS += ')))'
        elif c == '+':
            newS += ')+('
        elif c == '*':
            newS += '))*(('
        else:
            newS += c 
    newS += '))'
    return newS

def day18(s):
    t1 = 0
    t2 = 0
    for l in s:
        t1 += evaluateExpression(l)
        t2 += eval(addParens(l))
    return t1,t2
print(day18(s))