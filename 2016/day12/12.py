from collections import defaultdict

def runProgram(ins, p2flag):
    def get(x, regs):
        try:
            x = int(x)
        except ValueError:
            x = regs[x]
        return x
    regs = defaultdict(int)
    pointer = 0
    num_ins = len(ins)
    if p2flag:
        regs['c'] = 1
    while pointer < num_ins:
        cur_ins = ins[pointer]
        if cur_ins[0] == 'cpy':
            regs[cur_ins[2]] = get(cur_ins[1], regs)
        elif cur_ins[0] == 'inc':
            regs[cur_ins[1]] += 1
        elif cur_ins[0] == 'dec':
            regs[cur_ins[1]] -= 1
        elif cur_ins[0] == 'jnz':
            val1 = get(cur_ins[1], regs)
            val2 = get(cur_ins[2], regs)
            if val1 != 0:
                pointer += val2
                continue
        pointer += 1
    return regs

if __name__ == "__main__":
    file = 'input.txt'
    ins = [x.split(' ') for x in open(file).read().split('\n')]
    p1 = runProgram(ins, False)['a']
    p2 = runProgram(ins, True)['a']
    print(f"Part 1: {p1}\nPart 2: {p2}")