def manhattanDistance(p,q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])
text = open('input.txt','r').read().splitlines()
uBound = 400

coords = []
for t in text: 
    tmp = t.split(', ')
    coords.append( (int(tmp[0]), int(tmp[1])))

areas = [0]*len(coords)
infinite = [0]*len(coords)
part2area = 0

for x in range(uBound):
    for y in range(uBound):
        distances = [manhattanDistance((x,y),c) for c in coords]
        minDistance = min(distances)
        if distances.count(minDistance) == 1:
            index = distances.index(minDistance)
            areas[index] += 1
            #if a region touches the edge, it is infinite
            if x == uBound - 1 or x == 0 or y == 0 or y == uBound - 1:
                infinite[index] = 1
        if sum(distances) < 10000:
            part2area += 1
#zero out areas that are infinite so that they don't count
for i in range(len(areas)):
    areas[i] = 0 if infinite[i] else areas[i]
print "Part 1:", max(areas)
print "Part 2:", part2area