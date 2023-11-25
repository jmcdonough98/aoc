from itertools import product
s = open('input.txt','r').read().split('\n')

def applyMask(mask,n):
    nstr = list("{:b}".format(n).rjust(36,'0'))
    for i in range(len(mask)):
        if mask[i] != 'X':
            nstr[i] = mask[i]
    return "".join(nstr)

def applyMask2(mask,n):
    nstr = list("{:b}".format(n).rjust(36,'0'))
    floating = []
    addresses = []
    for i in range(len(mask)):
        if mask[i] == '1':
            nstr[i] = '1'
        elif mask[i] == 'X':
            floating.append(i)
    fmask = list(product("01",repeat = len(floating)))
    for j in range(len(fmask)):
        for i in range(len(floating)):
            nstr[floating[i]] = fmask[j][i]
        addresses.append(int("".join(nstr),2))
    return addresses

def day14(s):
    mem1 = {}
    mem2 = {}
    for l in s:
        if l[:4] == 'mask':
            mask = l[7:]
        else:
            tmp = l.split(' = ')
            addr = int(tmp[0][4:-1])
            val = int(tmp[1])
            mem1[addr] = int(applyMask(mask,val),2)
            addresses = applyMask2(mask,addr)
            for a in addresses:
                mem2[a] = val
    return sum(mem1.values()),sum(mem2.values())

print(day14(s))