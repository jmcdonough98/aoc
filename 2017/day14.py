from functools import reduce

def knotStep(knot, lengths, currPos, skipSize):
    N = 256
    for l in lengths:
        if currPos + l < N:
            knot[currPos:currPos+l] = reversed(knot[currPos:currPos+l])
        else:
            d1 = N - currPos
            d2 = l - d1
            tmp = list(reversed(knot[currPos:currPos+d1] + knot[:d2]))
            knot[currPos:] = tmp[:d1]
            knot[:d2] = tmp[d1:]

        currPos = (currPos + skipSize + l) % N
        skipSize += 1
    return knot, currPos, skipSize

def knotHash(s):
    N = 256
    lengths = [ord(x) for x in s]
    lengths += [17,31,73,47,23]
    currPos = 0
    skipSize = 0
    knot = list(range(N))
    for hashRound in range(64):
        knot,currPos,skipSize = knotStep(knot, lengths, currPos, skipSize)
    dense = []
    for i in range(16):
        dense.append(reduce(lambda x,y: x^y, knot[16*i:16*(i+1)]))
    dense = [str(hex(x))[2:].zfill(2) for x in dense]
    return "".join(dense)
    
def hashToBinRow(r):
    tmp = []
    for char in r:
        tmp += [int(x) for x in list(bin(int(char,16))[2:].zfill(4))]
    return tmp

def makeGrid(inputStr):
    grid = []

    for i in range(128):
        row = knotHash(inputStr + "-" + str(i))
        grid.append(hashToBinRow(row))
    return grid

def findRegions(grid):
    N = len(grid)
    seen = set()
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] and (i,j) not in seen:
                count += 1
                boundary = [(i,j)]
                while len(boundary) > 0:
                    tmp = set()
                    for (x,y) in boundary:
                        if x >= 1 and grid[x-1][y]:
                            if ((x-1,y)) not in seen:
                                tmp.add((x-1,y))
                                seen.add((x-1,y))
                        if x < N -1 and grid[x+1][y]:
                            if ((x+1,y) not in seen):
                                tmp.add((x+1,y))
                                seen.add((x+1,y))
                        if y >= 1 and grid[x][y-1]:
                            if ((x,y-1) not in seen):
                                tmp.add((x,y-1))
                                seen.add((x,y-1))
                        if y < N - 1 and grid[x][y+1]:
                            if ((x,y+1) not in seen):
                                tmp.add((x,y+1))
                                seen.add((x,y+1))
                    boundary = list(tmp)
    return count
if __name__ == "__main__":
    grid = makeGrid("ugkiagan")
    print("Part 1:", sum(sum(x) for x in grid))
    print("Part 2:", findRegions(grid))