def p1(grid):
    ans = 0
    hits = [['X','M','A', 'S'], ['S','A','M','X']]
    for r in range(len(grid)-3):
        for c in range(len(grid[r])-3):
            diag = [grid[r+i][c+i] for i in range(4)]
            if diag in hits:
                ans += 1
    for r in range(3, len(grid)):
        for c in range(len(grid)-3):
            diag = [grid[r-i][c+i] for i in range(4)]
            if diag in hits:
                ans += 1
    for r in range(len(grid)):
        for c in range(len(grid) - 3):
            if grid[r][c:c+4] in hits:
                ans += 1
    for r in range(len(grid)-3):
        for c in range(len(grid)):
            if [grid[r+i][c] for i in range(4)] in hits:
                ans += 1
    return ans

def p2(grid):
    ans = 0
    for r in range(1,len(grid) - 1):
        for c in range(1, len(grid) - 1):
            x = [grid[r][c],grid[r-1][c-1], grid[r-1][c+1], grid[r+1][c-1], grid[r+1][c+1]]
            if x[0] == 'A' and sorted(x) == ["A","M","M","S","S"] and x[1] != x[4] :
                ans += 1
    return ans

if __name__ == "__main__":

    _input = open('input.txt','r').read().split('\n')
    grid = [list(l) for l in _input]
    a1, a2 = p1(grid), p2(grid)
    print("Part 1:", a1)
    print("Part 2:", a2)