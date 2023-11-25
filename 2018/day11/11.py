
def calcPower(x,y,s):
    rId = x+10
    return ((((y*rId + s) * rId) / 100) % 10) - 5
def populateGrid(maxSize,serial):
    grid = []
    for y in range(1,max + 1):
        line = []
        for x in range(1,max  +1 ):
            line.append(calcPower(x,y,serial))
        grid.append(line)
    return grid
def findMaxCell(grid,size):
    maxCell = (-100,0,0,size)
    for x in range(max + 1 - size):
        for y in range(max + 1 - size):
            square = sum([sum(powerGrid[i][x:x+size]) for i in range(y,y+size)] )
            if square > maxCell[0]:
                maxCell = (square,x+1,y+1,size)
    return maxCell
def findMaxCellSize(grid):
    answer = (-100,0,0,-1)
    for size in range(1,30):
        print size
        tmp = findMaxCell(grid,size)
        if tmp[0] > answer[0]:
            answer = tmp
    return answer
serial = 9798
s1 = 42
max = 301
powerGrid = populateGrid(max,serial)
answer = findMaxCellSize(powerGrid)
print answer
# print ((122+ 10 )* 79 + 57)*(122 + 10) % 100 % 10 - 5