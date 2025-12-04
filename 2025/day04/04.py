def valid(x,y, w,h):
    return 0 <= x < w and 0 <= y < h

def neighbors(x,y, w, h):
    return [p for p in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)] if valid(*p, w, h)]

def removePaper(grid, gridW, gridH):
    removable = []
    for y in range(gridH):
        for x in range(gridW):
            if grid[y][x] == '.':
                continue
            pc = 0
            for (xp,yp) in neighbors(x,y, gridW, gridH):
                if grid[yp][xp] == '@':
                    pc += 1
            if pc < 4:
                removable.append((x,y))
    for (x,y) in removable:
        grid[y][x] = '.'
    return grid, len(removable)


file = "input.txt"
grid = [list(x) for x in open(file, 'r').read().split('\n')]
gridW = len(grid[0])
gridH = len(grid)

c = 0
removed = 1
rvals = []

while removed != 0:
    grid, removed = removePaper(grid, gridW, gridH)
    rvals.append(removed)

print(f"Part 1: {rvals[0]}\nPart 2: {sum(rvals)}")