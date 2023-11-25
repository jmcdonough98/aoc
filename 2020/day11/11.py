from copy import deepcopy
g = [list(x) for x in open('input.txt','r').read().split('\n')]

def adjCount(g,y,x):
    c = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 or i != j:
                if 0 <= y + i < len(g) and 0 <= x + j < len(g[0]):
                    c += (g[y+i][x+j] == '#')
    return c

def p2adjCount(g,y,x):
    c = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 or i != j:
                n = 1
                while True:
                    if 0 <= y + (n*i) < len(g) and 0 <= x + (n*j) < len(g[0]):
                        if (g[y+(n*i)][x+(n*j)] == '#'):
                            c += 1
                            break
                        elif (g[y+(n*i)][x+(n*j)] == 'L'):
                            break
                    else:
                        break
                    n += 1
    return c

def iterateGrid(g,f,tolerance):
    g2 = deepcopy(g)
    for y in range(len(g)):
        for x in range(len(g[y])):
            if g[y][x] == 'L' and f(g,y,x) == 0:
                g2[y][x] = '#'
            elif g[y][x] == '#' and f(g,y,x) >= tolerance:
                g2[y][x] = 'L'
    return g2

def countSeats(g):
    count = 0
    for r in g:
        for c in r:
            if c == '#':
                count += 1
    return count

def simulateUntilFixed(g,adjacencyFunc = adjCount,tolerance = 4):
    count = 0
    prevCount = -1 
    while count != prevCount:
        prevCount = count
        g = iterateGrid(g,adjacencyFunc,tolerance)
        count = countSeats(g)
    return count

print(simulateUntilFixed(g,adjCount,tolerance = 4))
print(simulateUntilFixed(g,p2adjCount,tolerance = 5))