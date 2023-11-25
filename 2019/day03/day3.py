with open("input.txt","r") as f:
    parsed = [x.split(",") for x in f.read().split("\n")][:2]
    line1 = parsed[0]
    line2 = parsed[1]

#find all intersections using my gross tuple construction
def findIntersections(C1,C2):
    I = []
    for i in range(len(C1)-1):
        for j in range(len(C2)-1):
            if C1[i+1][0] == C2[j+1][0]: # Both lines same direction = no intersection
                continue
            elif C1[i+1][0] == 'H': #C1 Horiz C2 Vert
                X = isIntersection(C1[i][1],C1[i+1][1],C2[j][1],C2[j+1][1], C1[i][2],C2[j][2])
            else: #C1 Vert C2 Horiz
                X = isIntersection(C2[j][1],C2[j+1][1],C1[i][1],C1[i+1][1], C2[j][2],C1[i][2])

            if X != False:
                I.append(X)
    return I
#p1 -> p2 is horizontal p3 -> p4 is vertical
#check if the 2 lines created are intersecting
def isIntersection(p1,p2,p3,p4,d1,d2):
    (x1,y1) = p1
    (x2,y2) = p2
    (x3,y3) = p3
    (x4,y4) = p4
    if min(x1,x2) <= x3 and x3 <= max(x1,x2) and min(y3,y4) <= y1 and y1 <= max(y3,y4):
        return ((x3,y1),d1 + abs(x3-x1),d2 + abs(y3-y1))
    return False

#find minimum manhattan distance from a list of tuples
def closestIntersection(I):
    d = abs(I[0][0]) + abs(I[0][1])
    for isct in I:
        if abs(isct[0]) + abs(isct[1]) < d:
            d = abs(isct[0]) + abs(isct[1])
    return d
#Turn program input into a list of tuples: (Orientation, coordinate of endpoint, total distance thus far)
def parseLine(line):
    C = []
    x, y = 0, 0
    distance = 0
    for l in line:
        direction = l[0]
        value = int(l[1:])
        distance += value
        if direction == 'R':
            x += value
        elif direction == 'L':
            x -= value  
        elif direction == 'U':
            y += value    
        elif direction == 'D':
            y -= value

        if direction == 'R' or direction == 'L':     
            C.append(('H',(x,y),distance))
        else:
            C.append(('V',(x,y),distance))
    return C

C1 = parseLine(line1)
C2 = parseLine(line2)
I = findIntersections(C1,C2)
print("PART1:", closestIntersection([x[0] for x in I]))
print("PART2:", min( [x[1] + x[2] for x in I]))