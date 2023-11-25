with open('input.txt','r') as f:
    s = f.read().split('\n')

def day2(s):
    p1count = 0
    p2count = 0
    for l in s:
        ll = l.split(' ')
        m,M = [int(x) for x in ll[0].split('-')]
        c = ll[1][0]
        charCount = ll[2].count(c)
        p1count += charCount <= M and charCount >= m
        p2count += (ll[2][m-1] == c) ^ (ll[2][M-1]==c)
    return p1count,p2count

print(day2(s))
