s = open('input.txt','r').read().split('\n')
import math

def part1(s):
    x,y = 0,0
    currDir = 0
    for l in s:
        dire = l[0]
        val = int(l[1:])
        if dire == 'E':
            x += val
        elif dire == 'W':
            x -= val
        elif dire == 'N':
            y += val
        elif dire == "S":
            y -= val
        elif dire == "R":
            currDir += (val / 90) % 4
            currDir %= 4
        elif dire == 'L':
            currDir += ((360 - val) / 90)
            currDir %= 4
        elif dire == 'F':
            if currDir == 0:
                x += val
            elif currDir == 1:
                y -= val
            elif currDir == 2:
                x -= val
            elif currDir == 3:
                y += val
    return abs(x) + abs(y)
def rotateWayPoint(x,y,wx,wy,r):
    return wx*int(math.cos(r)) - wy*int(math.sin(r)), wx*int(math.sin(r)) + wy*int(math.cos(r))
def part2(s):
    x,y = 0,0
    wx,wy = 10,1
    currDir = 0
    for l in s:
        dire = l[0]
        val = int(l[1:])
        if dire == 'E':
            wx += val
        elif dire == 'W':
            wx -= val
        elif dire == 'N':
            wy += val
        elif dire == "S":
            wy -= val
        elif dire == "R":
            val = 360 - val
            wx,wy = rotateWayPoint(x,y,wx,wy,math.radians(val))
        elif dire == 'L':
            wx,wy = rotateWayPoint(x,y,wx,wy,math.radians(val))
        elif dire == 'F':
            x += val*wx
            y += val*wy
    return abs(x) + abs(y)


print(part1(s), part2(s))
