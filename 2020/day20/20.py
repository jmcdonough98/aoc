import re
from collections import defaultdict
import numpy as np
from copy import copy

def parseInput(s):
    pattern = r"Tile (\d+):\n"
    tiles = {}
    for l in s:
        tileID = int(re.match(pattern,l).groups(0)[0])
        tileGrid = []
        for row in l.split('\n')[1:]:
            tmp = []
            for col in row:
                tmp.append(int(col=='#'))
            tileGrid.append(tmp)
        tiles[tileID] = tileGrid
    return tiles

def findStartingOrientation(tiles,initID):
    rootTile = tiles.pop(initID)
    orientations = D8(rootTile)
    tmp = None
    for o in orientations:
        tmp = buildGrid(copy(tiles),initID,o)
        if tmp != None:
            return tmp
    return tmp
def buildGrid(tiles, rootId, root, size = 12):
    #initial ID = 2239 for actual input, 1951 for test input
    # initID = 1951
    idGrid = [[rootId]]
    tileGrid = [[root]]

    for row in range(size):
        if row > 0:
            side = tileGrid[row - 1][0][-1]
            flag = True
            for tileID in tiles:
                tmp = checkTileOrientations(tiles[tileID],side,True)
                if tmp != None:
                    flag = False
                    idGrid.append([tileID])
                    tileGrid.append([tmp])
                    tiles.pop(tileID)
                    break
            if flag:
                return None
        for col in range(1,size):
            flag = True
            side = [x[-1] for x in tileGrid[row][col - 1]]
            for tileID in tiles:
                tmp = checkTileOrientations(tiles[tileID],side,False)
                if tmp != None:
                    idGrid[row].append(tileID)
                    tileGrid[row].append(tmp)
                    tiles.pop(tileID)
                    flag = False
                    break
            if flag:
                return None
    return idGrid,tileGrid
# return correct orientation if it works, None if none were found 
# flag indicates whether we are checking the top side of the tile (for starting a new row) or the left (for continuing a row)
def checkTileOrientations(g, side,flag):
    d8 = D8(g)
    for i in range(len(d8)):
        if flag and side == d8[i][0]:
            return d8[i]
        if (not flag) and side == [x[0] for x in d8[i]]:
            return d8[i]
    return None

def f(g):
    newG = []
    for i in range(len(g)-1,-1,-1):
        newG.append(g[i])
    return newG

def r(g):
    newG = []
    for i in range(len(g)):
        newG.append(list(reversed([x[i] for x in g])))
    return newG
def D8(g):
    return [g,r(g),r(r(g)),r(r(r(g))), f(g), r(f(g)),r(r(f(g))),r(r(r(f(g))))]


trim = lambda t: [x[1:-1] for x in t[1:-1]]
def makeImage(tiles):
    im = np.array([])
    for i in range(len(tiles)):
        tmpRow = np.array(trim(tiles[i][0]))
        for j in range(1,len(tiles)):
            tmpRow = np.concatenate((tmpRow,trim(tiles[i][j])),axis = 1)
        if i == 0:
            im = tmpRow
        else:
            im = np.concatenate((im,tmpRow),axis = 0)
    return im

def findSeaMonster(im):
    h = 3
    l = 20
    mask = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                     [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
                     [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]])
    total = np.sum(im)
    for x in D8(im):
        x = np.array(x)
        count = 0
        for i in range(len(x)):
            for j in range(len(x[0])):
                sub = x[i:i+h, j:j+l]
                try:
                    if sum([np.dot(sub[k],mask[k]) for k in range(h)] ) == 15:
                        count += 1
                except:
                    pass
        if count > 0:
            return total - 15*count
s = open('input.txt','r').read().split('\n\n')    
tiles = parseInput(s)
i,t =findStartingOrientation(tiles,2239)
print("Part 1:", i[0][0] * i[0][-1] * i[-1][0] * i[-1][-1])

im = makeImage(t)
print("Part 2:", findSeaMonster(im))