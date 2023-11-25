from itertools import combinations
import numpy as np
weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armor = [(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
rings = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]

def fight(pDam, pArm, pHP, bDam, bArm, bHP):
    pRounds = np.ceil(bHP / max(1,(pDam - bArm)))
    bRounds = np.ceil(pHP / max(1,(bDam - pArm))) 
    return pRounds <= bRounds

def testLoadout(w,a,r,pHP,bDam,bArm,bHP):
    cost, dam, arm = w[0],w[1],w[2]
    for x in a:
        cost += x[0]
        dam += x[1]
        arm += x[2]
    for x in r:
        cost += x[0]
        dam += x[1]
        arm += x[2]
    if fight(dam,arm,pHP, bDam, bArm, bHP):
        return True, cost
    return False, cost


def p1(pHP,bDam,bArm,bHP):
    minCost = 1000
    maxCost = 0
    for w in weapons:
        for j in range(2):
            for a in combinations(armor,j):
                for i in range(3):
                    for r in combinations(rings, i):
                        f,c = testLoadout(w,a,r,pHP,bDam,bArm,bHP)
                        if f and c < minCost:
                            minCost = c
                        if not f and c > maxCost:
                            maxCost = c
    return minCost,maxCost
print(p1(100,9,2,103))