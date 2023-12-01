_input = "L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2"



def part1(_in):
    rules = {"L":-1, "R":1}
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    pos = (0,0)
    idx = 0
    for x in _in:
        idx = (idx + rules[x[0]]) % 4
        scale = int(x[1:])
        pos = (pos[0] + dirs[idx][0]* scale, pos[1] + dirs[idx][1]*scale) 
    return abs(pos[0]) + abs(pos[1])
def part2(_in):
    rules = {"L":-1, "R":1}
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    pos = (0,0)
    idx = 0
    visited = set()
    for x in _in:
        idx = (idx + rules[x[0]]) % 4
        scale = int(x[1:])
        for i in range(1,scale+1):
            tmp = (pos[0] + dirs[idx][0]*i, pos[1] + dirs[idx][1]*i) 
            if tmp in visited:
                return abs(tmp[0]) + abs(tmp[1])
            visited.add(tmp)
        pos = tmp
if __name__ == "__main__":
    _input = _input.split(', ')
    print("Part 1:", part1(_input))
    print("Part 2:", part2(_input))