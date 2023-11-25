from itertools import takewhile

def checkVis(grid):
    visible = [[0]*len(x) for x in grid]
    for i in range(len(grid)):
        row = grid[i]
        for j in range(1,len(row)):
            if row[j] > max(row[:j]):
                visible[i][j] = 1
            if row[-j] > max(row[-j+1:]):
                visible[i][-j] = 1
    for j in range(len(grid[0])):
        col = [grid[x][j] for x in range(len(grid))]
        for i in range(1,len(col)):
            if col[i] > max(col[:i]):
                visible[i][j] = 1
            if col[-i] > max(col[-i+1:]):
                visible[-i][j] = 1
    visible[0] = [1]*len(grid)
    visible[-1] = [1]*len(grid)
    for i in range(len(grid)):
        visible[i][0] = 1
        visible[i][-1] = 1

    print("Part 1:", sum(sum(x) for x in visible))
def checkVis2(grid):
    scores = [[0]*len(grid) for x in grid]
    score = lambda val, run: min(1 + len(list(takewhile(lambda x: x < val, run))),len(run))
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid)-1):
            right = grid[i][j+1:]
            left = grid[i][:j][::-1]
            up = [grid[x][j] for x in range(i)][::-1]
            down = [grid[x][j] for x in range(i+1,len(grid))]
            val = grid[i][j]
            scores[i][j] = score(val,up)*score(val,down)*score(val,right)*score(val,left)
    print("Part 2:", max(max(x) for x in scores))

if __name__ == "__main__":
    grid = [[int(x) for x in y] for y in open('input.txt','r').read().split('\n')]

    checkVis(grid)
    checkVis2(grid)
