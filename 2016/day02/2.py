"""
val: dictionary with keys valid (x,y) positions, and values corresponding to the button at that position
dirs: vector to add to current position given a direction
pos: initial position
validPos: function determining whether a given vector is a valid position
s: list of instructions
"""
def enterCode(val, dirs, pos, validPos, s):
    code = ""
    for line in s:
        for ch in line:
            tmp = (pos[0] + dirs[ch][0], pos[1] + dirs[ch][1])
            pos = tmp if validPos(tmp) else pos
        code += val[pos]
    return code

if __name__ == "__main__":
    s = open('input.txt','r').read().split('\n')

    print("Part 1:", enterCode(
        {(x,y): str(3*y + x + 1) for x in range(3) for y in range(3)},
        {"U":(0,-1), "L":(-1,0), "D":(0,1), "R":(1,0)},
        (1,1),
        lambda pos: 0 <= pos[0] <= 2 and 0 <= pos[1] <= 2,
        s
    ))

    print("Part 2:", enterCode(
        {(0,2): "1", (-1,1):"2", (0,1):"3", (1,1):"4", (-2,0):"5", (-1,0):"6",(0,0):"7",(1,0):"8",(2,0):"9", (-1,-1):"A",(0,-1):"B",(1,-1):"C", (0,-2):"D"},
        {"U":(0,1), "L":(-1,0), "D":(0,-1), "R":(1,0)},
        (-2,0),
        lambda pos: abs(pos[0]) + abs(pos[1]) <= 2,
        s
    ))