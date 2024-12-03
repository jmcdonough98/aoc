import re

def rect(GRID,x,y):
    for i in range(x):
        for j in range(y):
            GRID[j][i] = 1

def rcol(GRID, col, amt):
    tmp = [GRID[i][col] for i in range(len(GRID))]
    for i in range(len(GRID)):
        GRID[i][col] = tmp[(i -amt) % HEIGHT]

def rrow(GRID,row, amt):
    amt %= WIDTH
    GRID[row] = GRID[row][WIDTH - amt:]  +GRID[row][:WIDTH - amt] 

def parseIns(ins,GRID):
    tmp = re.match(r"^rect (\d+)x(\d+)$", ins)
    if tmp:
        rect(GRID, int(tmp.group(1)),int(tmp.group(2)))
    tmp = re.match(r"^rotate column x=(\d+) by (\d+)", ins)
    if tmp:
        rcol(GRID, int(tmp.group(1)),int(tmp.group(2)))
    tmp = re.match(r"^rotate row y=(\d+) by (\d+)", ins)
    if tmp:
        rrow(GRID, int(tmp.group(1)),int(tmp.group(2)))
    
def printGrid(GRID):
    
    dic = {0:"□",1:"■"}
    print()
    for r in GRID:
        for c in r:
            print(dic[c],end="")
        print()
    print()

if __name__ == "__main__":

    WIDTH, HEIGHT = 50,6
    GRID = [[0]*WIDTH for i in range(HEIGHT)]
    _input = open('input.txt','r').read().split('\n')
    for ins in _input:
        parseIns(ins,GRID)
    print("Part 1:", sum(sum(r) for r in GRID))
    print("Part 2:")
    printGrid(GRID)