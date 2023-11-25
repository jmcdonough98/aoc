from functools import reduce

def score():
    score = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if r > 0 and grid[r][c] >= grid[r-1][c]:
                continue 
            if r < len(grid) - 1 and grid[r][c] >= grid[r+1][c]:
                continue 
            if c > 0 and grid[r][c] >= grid[r][c-1]:
                continue 
            if c < len(grid[0]) - 1 and grid[r][c] >= grid[r][c+1]:
                continue 
            score += 1 + grid[r][c]
    return score

def findBasins(grid):
    basins = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if any((r,c) in x for x in basins) or grid[r][c] == 9:
                continue 
            else:
                currBasin = set()
                currBasin.add(tuple([r,c]))
                changed = True
                while changed:
                    changed = False
                    for coord in list(currBasin):
                        rx = coord[0]
                        cx = coord[1]
                        if cx > 0 and grid[rx][cx-1] != 9 and (rx,cx-1) not in currBasin:
                            currBasin.add(tuple([rx,cx-1]))
                            changed = True

                        if cx <  len(grid[0]) - 1 and grid[rx][cx+1] != 9 and (rx,cx+1) not in currBasin:
                            currBasin.add(tuple([rx,cx+1]))
                            changed = True

                        if rx > 0 and grid[rx-1][cx] != 9 and (rx-1,cx) not in currBasin:
                            currBasin.add(tuple([rx-1,cx]))
                            changed = True

                        if rx < len(grid) - 1 and grid[rx+1][cx] != 9 and (rx+1,cx) not in currBasin:
                            currBasin.add(tuple([rx+1,cx]))
                            changed = True
                basins.append(currBasin)
    return basins


lines = open('input.txt','r').read().split('\n')
grid = []
for l in lines:
    grid.append([int(x) for x in l])

print(score())
basins = findBasins(grid)
print(reduce(lambda x,y: x*y, sorted(list(map(len, findBasins(grid))))[-3:]   ))