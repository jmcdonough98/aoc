lines = open('test.txt','r').read().split('\n')

grid = []
for l in lines:
    grid.append([int(x) for x in l])
print(grid)


def testPoint(x,y, grid, flashed):
    grid[x][y] += 1
    if grid[x][y] == 10:
        grid[x][y] = 0
        return tuple([x,y]), True
    return tuple([x,y]), False

def step():
    flashed = set()
    fc = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1
            if grid[i][j] == 10:
                flashed.add(tuple([i,j]))
                grid[i][j] = 0
    print(flashed)
    flag = True
    added = set()
    while flag:
        flag = False 
        # newf = copy(flashed)
        newf = set()
        for c in flashed:
            if c in added:
                continue
            cx = c[0]
            cy = c[1]
            if cx > 0:
                a,b = testPoint(cx-1,cy,grid,flashed)
                if b:
                    newf.add(a)
                if cy > 0:
                    a,b = testPoint(cx-1,cy-1,grid,flashed)
                    if b:
                        newf.add(a)
                    a,b = testPoint(cx,cy-1,grid,flashed)
                    if b:
                        newf.add(a)
                if cy < 8:
                    a,b = testPoint(cx-1,cy+1,grid,flashed)
                    if b:
                        newf.add(a)
                    a,b = testPoint(cx,cy+1,grid,flashed)
                    if b:
                        newf.add(a)
            elif cx < 8:
                a,b = testPoint(cx+1,cy,grid,flashed)
                if b:
                    newf.add(a)
                if cy > 0:
                    a,b = testPoint(cx+1,cy-1,grid,flashed)
                    if b:
                        newf.add(a)
                if cy < 8:
                    a,b = testPoint(cx+1,cy+1,grid,flashed)
                    if b:
                        newf.add(a)
            added.add(c)
            flag = True
        flashed = flashed.union(newf)
    return len(flashed)

c = 0
for i in range(100):
    c += step()
    print(c)
print(c)