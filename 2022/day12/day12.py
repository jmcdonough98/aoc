from math import inf

def makeGrid():
    s = open('input.txt','r').read().split('\n')
    grid = [[0]*len(s[0]) for x in s]
    S = None
    E = None
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 'S':
                S = (i,j)
                grid[i][j] = 0
            elif s[i][j] == 'E':
                E = (i,j)
                grid[i][j] = 25
            else:
                grid[i][j] = ord(s[i][j]) - 97
    return grid, S, E

def neighbors(pt, cols, rows):
    x,y = pt
    tmp = []
    if x > 0:
        tmp.append((x-1, y))
    if x < rows - 1:
        tmp.append((x+1,y))
    if y > 0:
        tmp.append((x,y-1))
    if y < cols - 1:
        tmp.append((x,y+1))
    return tmp


def findPaths(S,E, grid):
    cols = len(grid[0])
    rows = len(grid)
    minDists = [[inf]*cols for x in grid]
    minDists[E[0]][E[1]] = 0

    points = [(i,j) for i in range(rows) for j in range(cols)]
    while len(points) != 0:
        currVertex = min(points, key = lambda x: minDists[x[0]][x[1]])
        points.remove(currVertex)
        for (x,y) in neighbors(currVertex, cols, rows):
            if grid[currVertex[0]][currVertex[1]] - grid[x][y] <= 1:
                candidate = minDists[currVertex[0]][currVertex[1]] + 1 
                if candidate < minDists[x][y]:
                    minDists[x][y] = candidate

    print("Part 1:", minDists[S[0]][S[1]])
    pt2 = min([(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 0], key = lambda x: minDists[x[0]][x[1]] )
    print("Part 2:", minDists[pt2[0]][pt2[1]])

if __name__ == '__main__':
    grid, S, E = makeGrid()
    findPaths(S,E,grid)
