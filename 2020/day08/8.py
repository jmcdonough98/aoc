def parseInput(filename):
    s = open(filename,'r').read().split('\n')
    ins_list = []
    for l in s:
        x,y = l.split(' ')
        ins_list.append((x,int(y)))
    return ins_list
def runProgram(ins_list):
    pc = 0
    acc = 0
    seen = set()
    while 1:
        if pc in seen:
            return acc, False # infinite loop, exit
        if pc >= len(ins_list):
            return acc, True # successfully exit
        ins,val = ins_list[pc]
        seen.add(pc)
        if ins == 'nop':
            pc += 1
        elif ins == 'acc':
            acc += val
            pc += 1
        else:
            pc += val   
    return acc
def findErrorBruteForce(ins_list):
    for i,ins in enumerate(ins_list):
        if ins[0] == 'nop':
            new_ins = ('jmp',ins[1])
        elif ins[0] == 'jmp':
            new_ins = ('nop',ins[1])
        else:
            continue
        ins_list[i] = new_ins
        val,status = runProgram(ins_list)
        ins_list[i] = ins
        if status:
            return val
    return None #not found
ins_list = parseInput('input.txt')
print('PART1:', runProgram(ins_list)[0])
print('PART2:', findErrorBruteForce(ins_list))