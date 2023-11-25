def parseWalls():
    s = open('input.txt','r').read().split('\n')
    walls = set()

    for line in s:
        pts = list(map(eval, line.split(' -> ')))
        for i in range(len(pts) - 1):
            if pts[i][0] == pts[i+1][0]:
                b = sorted([pts[i][1], pts[i+1][1]])
                walls = walls.union([(pts[i][0], x) for x in range(b[0], b[1] + 1)])
            if pts[i][1] == pts[i+1][1]:
                b = sorted([pts[i][0], pts[i+1][0]])
                walls = walls.union([(x, pts[i][1]) for x in range(b[0], b[1] + 1)])
    return walls
def simulateSand(walls):
    floor = max(walls, key = lambda x: x[1])[1] + 2
    sandCoords = set()
    p1flag = True
    while True:
        cs= (500,0)
        while True:
            if cs[1] > floor - 2 and p1flag:
                p1flag = False
                print("Part 1:", len(sandCoords))
            tmp = (cs[0], cs[1] +1)
            tmp2 = (cs[0] - 1, cs[1] +1)
            tmp3 = (cs[0] +1, cs[1] + 1)

            if tmp not in sandCoords and tmp not in walls and tmp[1] < floor:
                cs = tmp
            elif tmp2 not in sandCoords and tmp2 not in walls and tmp2[1] < floor:
                cs = tmp2
            elif tmp3 not in sandCoords and tmp3 not in walls and tmp3[1] < floor:
                cs = tmp3
            else:
                sandCoords.add(cs)
                break
        if cs == (500,0):
            print("Part 2:", len(sandCoords))
            return

if __name__ == "__main__":
    simulateSand(parseWalls())