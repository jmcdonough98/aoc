from collections import defaultdict

class tablet:
    def __init__(self, program, pid):
        self.program = program
        self.counter = 0
        self.registers = defaultdict(int)
        self.registers["p"] = pid
        self.queue = []
        self.waiting = False
        self.sendcounter = 0
        self.counter_offset = 1
        self.lastsent = None
        
    def run(self):
        self.counter_offset = 1
        ins = self.program[self.counter]
        arg1 = ins[1]

        if len(ins) == 3:
            arg1 = ins[1]
            arg2 = ins[2] if isinstance(ins[2], int) else self.registers[ins[2]]
            if ins[0] == "add":
                self.registers[arg1] += arg2
            elif ins[0] == "mul":
                self.registers[arg1] *= arg2
            elif ins[0] == "mod":
                self.registers[arg1] = self.registers[arg1] % arg2
            elif ins[0] == "set":
                self.registers[arg1] = arg2 
            elif ins[0] == "jgz":
                if isinstance(arg1,str):
                    arg1 = self.registers[arg1]
                if arg1 > 0:
                    self.counter_offset = arg2
        else:
            if ins[0] == "snd":
                if isinstance(arg1,str):
                    arg1 = self.registers[arg1]
                self.lastsent = arg1
                self.counter += self.counter_offset
                self.sendcounter += 1
                return arg1
            elif ins[0] == "rcv":
                if len(self.queue) == 0:
                    if self.waiting: # if the tablet was already waiting, both are waiting
                        return "t" 
                    self.waiting = True
                    return "w" 
                self.waiting = False
                self.registers[arg1] = self.queue.pop(0)
        self.counter += self.counter_offset

def parse_instructions(filename):
    program = []
    for l in open(filename, 'r').read().split('\n'):
        tmp = l.split(' ')
        try:
            tmp[-1] = int(tmp[-1])
        except:
            pass 
        if len(tmp) > 2: 
            try:
                tmp[-2] = int(tmp[-2]) #FUCK FUCK FUCK FUCK
            except:
                pass 
        program.append(tmp)
    return program

def part1(prog):
    tab = tablet(prog,0)
    while True:
        if tab.run() == "w":
            return tab.lastsent

def part2(prog):
    tabs = [tablet(prog,0),tablet(prog,1)]
    tmp = len(tabs[0].queue)
    pid = 0
    while True:
        res = tabs[pid].run()
        if isinstance(res, int):
            tabs[pid ^ 1].queue.append(res)
        elif res == "w": # tablet waiting for rcv
            pid ^= 1
        elif res == "t": # tablet terminated
            break 
    return tabs[1].sendcounter

if __name__ == "__main__":
    prog = parse_instructions('input.txt')
    print("Part 1:", part1(prog))
    print("Part 2:", part2(prog))
