s = [x.split(' ') for x in open('input.txt','r').read().split('\n')]

def parseIns(ins,a):
    regs = {}
    regs['a'], regs['b'] = a,0
    i = 0
    while i < len(ins):
        currIns = ins[i]
        if len(currIns) == 2:
            if currIns[0] == 'hlf':
                regs[currIns[1]] //= 2
            elif currIns[0] == 'tpl':
                regs[currIns[1]] *= 3
            elif currIns[0] == 'inc':
                regs[currIns[1]] += 1
            elif currIns[0] == 'jmp':
                i += eval(currIns[1]) 
                continue
            else:
                print("parse error")
        elif len(currIns) == 3:
            if currIns[0] == 'jio' and (regs[currIns[1][0]] == 1):
                i += eval(currIns[2])
                continue
            elif currIns[0] == 'jie' and (regs[currIns[1][0]] % 2 == 0):
                i += eval(currIns[2])
                continue
        i += 1
    return regs

print('PART 1:', parseIns(s, 0)['b'])
print('PART 2:', parseIns(s, 1)['b'])