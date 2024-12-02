lines = open('input.txt','r').read().split('\n')
a = [[int(x) for x in line.split(' ')] for line in lines]

def test(l):
    difs = [x-y for (x,y) in zip(l[:-1], l[1:])]
    return all(-3 <= x < 0 for x in difs) or all(3 >= x > 0 for x in difs)
def p1(lines):
    c = 0
    for l in lines:
        if test(l):
            c += 1
    return c
def p2(lines):
    c = 0
    for l in lines:
        for i in range(len(l)):
            if test(l[:i]+l[i+1:]):
                c+= 1
                break
    return c
print(p1(a))
print(p2(a))