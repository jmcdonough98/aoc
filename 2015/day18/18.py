from copy import deepcopy
def neighborSum(x,y,grid):
    count = 0
    for dx in range(-1,2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                if x + dx < 0 or y + dy < 0:
                    continue
                try:
                    if grid[y+dy][x+dx]:
                        count += 1
                except:
                    continue
    return count

def parseGrid(filename):
    with open(filename,'r') as f:
        lines = f.read().split('\n')
    grid = []
    for i in range(len(lines)):
        x = [0]*len(lines[i])
        for j,char in enumerate(lines[i]):
            if char == '#':
                x[j] = 1
        grid.append(x)
    return grid


def timeStep(grid,p2 = False):
    newGrid = deepcopy(grid) #inefficient, could instead use two copies of the grid and swap back and forth between them.
    for y in range(len(grid)):
        for x in range(len(grid)):
            c = neighborSum(x,y,grid)
            if grid[y][x]:
                if c != 2 and c != 3:
                    newGrid[y][x] = 0
                else:
                    newGrid[y][x] = 1
            else:
                if c == 3:
                    newGrid[y][x] = 1
                else:
                    newGrid[y][x] = 0
    if p2:
        newGrid[0][0] = 1
        newGrid[0][-1] = 1
        newGrid[-1][0] = 1
        newGrid[-1][-1] = 1
    return newGrid
def printGrid(grid):
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x]:
                print('#',end='')
            else:
                print('.',end='')
        print()

def countLights(grid):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            count += grid[y][x]
    return count

def solve(filename,stepCount): 
    p1,p2 = 0,0
    grid = parseGrid(filename)
    for i in range(stepCount):
        grid = timeStep(grid)
    p1 = countLights(grid)
    grid = parseGrid(filename)
    grid[0][0] = 1
    grid[0][-1] = 1
    grid[-1][0] = 1
    grid[-1][-1] = 1
    for i in range(stepCount):
        grid = timeStep(grid,True)
    p2 = countLights(grid)
    return (p1,p2)
print(solve('input.txt',100))