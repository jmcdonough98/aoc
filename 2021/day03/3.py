from copy import copy
lines = open('input.txt','r').read().split('\n')
N = len(lines[0])
def p1():
    g = ''
    e = ''
    for i in range(N):
        t1, t2 = determineBit(lines,i)
        g += t1
        e += t2
    return int(g,2) * int(e,2)

def pruneList(l,i,x):
    bit = determineBit(l,i)[x]
    new = []
    for ll in l:
        if ll[i] == bit:
            new.append(ll)
    return new
def determineBit(l, i):
    zc = 0
    oc = 0
    for ll in l:
        if ll[i] == '0':
            zc += 1
        else:
            oc += 1
    if zc > oc:
        return ('0','1')
    else:
        return ('1','0')
def p2():
    o_list = copy(lines)
    c_list = copy(lines)
    for j in range(N):
        if len(o_list) > 1:
            o_list = pruneList(o_list,j,0)
        if len(c_list) > 1:
            c_list = pruneList(c_list,j,1)
    return int(o_list[0],2)*int(c_list[0],2)

print(p1())
print(p2())