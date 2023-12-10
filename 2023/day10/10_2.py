def startPoint(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return (i,j)

adjPoints = lambda x: [(x[0],x[1] + 1), (x[0]+1,x[1]), (x[0],x[1]-1),(x[0]-1,x[1])] 

def connectedPoints(p, val):
    tmp = adjPoints(p)
    if val == "|":
        return [tmp[1], tmp[3]]
    elif val == "-":
        return [tmp[0], tmp[2]]
    elif val == "J":
        return [tmp[2], tmp[3]]
    elif val == "7":
        return [tmp[1], tmp[2]]
    elif val == "F":
        return [tmp[0], tmp[1]]
    elif val == "L":
        return [tmp[0], tmp[3]]
    return None

def part1(grid):
    # find S and one of the 2 points adjacent to S that connects to it.
    start = startPoint(grid)
    loop = [start]
    for p in adjPoints(start):
        if start in connectedPoints(p, grid[p[0]][p[1]]):
            loop.append(p)
            break
    # walk along the loop until we end up where we started
    while True:
        curr = loop[-1]
        a, b = connectedPoints(curr, grid[curr[0]][curr[1]])
        if a in loop and b in loop: # loop closed
            return loop 
        if a == loop[-2]:
            loop.append(b)
        if b == loop[-2]:
            loop.append(a)

def part2(loop, grid):
    start = loop[0]
    loop = loop
    # replace S with it's actual value
    for candidate in "|-LJ7F":
        if set(connectedPoints(start, candidate)) == set([loop[1], loop[-1]]):
            grid[start[0]] = grid[start[0]][:start[1]] + candidate + grid[start[0]][start[1]+1:]
            break
    loop = set(loop) # more efficient to check membership

    # for any point not on the loop, we can count the number of times we cross the boundary
    # going from the left edge of the grid. If this count is odd, the point is in the interior.
    # To count the boundary intersections, notice that we only need to consider 
    # if the grid value is a |, L, or J, since any others are redundant inforation
    # For instance, crossing F---J should count as crossing the boundary, whereas L---J shouldn't
    # (think about how they would continue on the lines above/below) 
    interiorCount = 0
    countGrid = [[0]* len(grid[0]) for x in grid]
    for i in range(len(grid)):
        countGrid[i][0] = int(grid[i][0] in "|LJ") if (i,0) in loop else 0
        for j in range(1,len(grid[0])):
            countGrid[i][j] = (countGrid[i][j-1] + (int(grid[i][j] in "|LJ") if (i,j) in loop else 0)) % 2
            if (i,j) not in loop and countGrid[i][j]:
                interiorCount += 1
    return interiorCount

if __name__ == "__main__":
    grid = open('input.txt','r').read().split('\n')
    loop = part1(grid)
    print("Part 1:", len(loop) // 2)
    print("Part 2:", part2(loop, grid))
