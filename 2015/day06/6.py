
def parseCoord(coord):
    x,y = coord.split(',')
    return (int(x),int(y))

def parseInstruction(strIns):
    parts = strIns.split(' ')
    code = 0
    x1,y1,x2,y2 = 0,0,0,0
    if len(parts) == 4:
        code = 2
        x1,y1 = parseCoord(parts[1])
        x2,y2 = parseCoord(parts[3])
    elif len(parts) == 5:
        if parts[1] == 'on':
            code = 0
        else:
            code = 1
        x1,y1 = parseCoord(parts[2])
        x2,y2 = parseCoord(parts[4])
    else: 
        print("FAILED PARSE",strIns)
    return (code,x1,y1,x2,y2)


def applyInstruction(ins, lights,simple):
    code, x1,y1,x2,y2 = ins
    if x1 > x2 or y1 > y2:
        print('a')
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if simple:
                if code == 0:
                    lights[i][j] = 1
                elif code == 1:
                    lights[i][j] = 0

                elif code == 2:
                    lights[i][j] ^= 1
            else:
                if code == 0:
                    lights[i][j] += 1
                elif code == 1:
                    lights[i][j] = max(0,lights[i][j] - 1)
                elif code == 2:
                    lights[i][j] += 2
def countLights(lights):
    count = 0
    for i in range(len(lights)):
        for j in range(len(lights)):
            count +=lights[i][j]
    return count
def part1(lights):
    for ins in instructions:
        applyInstruction(parseInstruction(ins),lights)
    return countLights(lights)

def solve():
    N = 1000
    lights = [[0 for x in range(N)] for x in range(N)]
    with open('input.txt') as f:
        instructions = f.read().split('\n')
    for ins in instructions:
        applyInstruction(parseInstruction(ins),lights,True)
    print('PART1:', countLights(lights))
    lights = [[0 for x in range(N)] for x in range(N)]
    for ins in instructions:
        applyInstruction(parseInstruction(ins),lights,False)
    print('PART2:', countLights(lights))

solve()

