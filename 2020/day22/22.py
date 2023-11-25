from copy import copy
s = open('input.txt','r').read().split('\n\n')

def parseCards(s):
    p1,p2 = [int(x) for x in s[0].split('\n')[1:]],[int(x) for x in s[1].split('\n')[1:]]
    return p1,p2

def scoreHand(p):
    score = 0
    for i in range(len(p)):
        score += (len(p) - i) * p[i]
    return score
def playGame(p1,p2):
    while len(p1) != 0 and len(p2) != 0:
        p1c = p1[0]
        p2c = p2[0]
        if p1c > p2c:
            p1 = p1[1:] + [p1c,p2c]
            p2 = p2[1:]
        else:
            p2 = p2[1:] + [p2c,p1c]
            p1 = p1[1:]
    if len(p1) == 0:
        return scoreHand(p2)
    return scoreHand(p1)

def playRecursive(p1,p2):
    seen = set()
    while len(p1) != 0 and len(p2) != 0:
        if (tuple(p1),tuple(p2)) in seen:
            return 0,0
        seen.add((tuple(p1),tuple(p2)))
        p1c = p1[0]
        p2c = p2[0]
        if p1c < len(p1) and p2c < len(p2):
            winner,score = playRecursive(copy(p1[1:1+p1c]),copy(p2[1:1+p2c]))
        else:
            winner = p1c < p2c
        if winner == 0:
            p1 = p1[1:] + [p1c,p2c]
            p2 = p2[1:]
        else:
            p2 = p2[1:] + [p2c,p1c]
            p1 = p1[1:]
    if len(p1) == 0:
        return 1,scoreHand(p2)
    return 0, scoreHand(p1)
p1,p2 = parseCards(s)
print(playGame(p1,p2))
p1,p2 = parseCards(s)
print(playRecursive(p1,p2))