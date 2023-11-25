import math

calcEnergy = lambda x : sum(map(abs, x))

def stepCoord(state):
    for j in range(4):
        for k in range(j+1,4):
            if state[j] < state[k]:
                state[j + 4] += 1
                state[k + 4] -= 1
            elif state[j] > state[k]:
                state[j + 4] -= 1
                state[k + 4] += 1    
    for j in range(4):
        state[j] += state[j+4]
    return state
def part1Sim(m1,m2,m3,m4):
    fullState = [[m1[i],m2[i],m3[i],m4[i],0,0,0,0 ] for i in range(3)]
    for i in range(1000):
        for j in range(3):
            fullState[j] = stepCoord(fullState[j])

    cols = [[fullState[x][i] for x in range(3)] for i in range(4)]
    cols2 = [[fullState[x][i] for x in range(3)] for i in range(4,8)]
    pE = map(calcEnergy,cols)
    kE = map(calcEnergy,cols2)
    print("PART1:",sum([a*b for a,b in zip(pE,kE) ]))

def simulateOneCoord(x1,x2,x3,x4):
    target = [x1,x2,x3,x4,0,0,0,0]
    state = [x1,x2,x3,x4,0,0,0,0]
    i = 0
    while state != target or i < 1:
        state = stepCoord(state)
        i += 1
    return i

def lcm(a,b,c):
    g1 = math.gcd(a,b)
    l1 = a*b // g1
    g2 = math.gcd(l1,c)
    return (a*b*c)//(g1*g2)

def findRepeat(m1,m2,m3,m4):
    repeats = [simulateOneCoord(m1[i],m2[i],m3[i],m4[i]) for i in range(3)]
    print("PART2:",lcm(repeats[0],repeats[1],repeats[2]))
part1Sim((-4, 3, 15),(-11, -10, 13),(2, 2, 18),(7, -1, 0))
findRepeat((-4, 3, 15),(-11, -10, 13),(2, 2, 18),(7, -1, 0))