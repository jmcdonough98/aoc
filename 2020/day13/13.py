from functools import reduce
s = open('input.txt','r').read().split('\n')

ns = []
for i,l in enumerate(s[1].split(',')):
    if l != 'x':
        ns.append((i,int(l)))

def p1(ns):
    i = int(s[0])
    start = i
    while True:
        for n in ns:
            if i % n == 0:
                return n*(i-start)
        i += 1  

def crt(ns):
    N = reduce(lambda x,y: x * y,[x[1] for x in ns])
    ai = [(-x[0]) % x[1] for x in ns ]
    ans = 0
    for i in range(len(ns)):
        s,t = extendedEuclid(ns[i][1],N // ns[i][1])
        ans += ai[i] * t * (N // ns[i][1])
    return ans % N

def extendedEuclid(a,b):
    os,s = 1,0
    ot,t = 0,1
    while b != 0:
        q = a // b
        a,b = b, a - b*q
        os,s = s, os - s*q
        ot,t = t, ot - t*q
    return os,ot

print(p1([x[1] for x in ns]))
print(crt(ns))