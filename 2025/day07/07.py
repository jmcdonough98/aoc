
file = 'input.txt'
grid = [list(x) for x in open(file).read().split('\n')]

R = len(grid)
C = len(grid[0])
p1c = 0
ways = [[0]*C for i in range(R)]
for i in range(C):
    if grid[0][i] == 'S':
        ways[0][i] = 1
for r in range(1,R):
    for c in range(C):
        if ways[r-1][c] != 0:
            if grid[r][c] == '^':
                ways[r][c-1] += ways[r-1][c]
                ways[r][c+1] += ways[r-1][c]
                p1c += 1
            else:
                ways[r][c] += ways[r-1][c]
print(f"Part 1: {p1c}\nPart 2: {sum(ways[-1])}")