from itertools import permutations
from copy import copy
with open("input.txt","r") as f:
    stream = [int(x) for x in f.read().split(",")]
def parseOpCode(n):
    codeVal = n % 100
    n //= 100
    modeA = n % 10
    n //= 10
    modeB = n % 10
    n //= 10
    modeC = n % 10 
    n //= 10
    return (codeVal,modeA,modeB,modeC)

class machine:
    def __init__(self,s,inputs,pc = 0):
        self.stream = s
        self.inputs = inputs
        self.pc = pc
        self.outVal = 0
    # Run intcode machine until it reachs an output or halts
    # Return (output, True) or (output, False) if halted
    def runUntilOutput(self,newInput):
        if newInput != []:
            self.inputs.append(newInput)
        while self.pc < len(self.stream):
            (code,ma,mb,_) = parseOpCode(self.stream[self.pc])
            try:
                va = self.stream[self.pc + 1] if ma == 1 else self.stream[self.stream[self.pc + 1]]
                vb = self.stream[self.pc + 2] if mb == 1 else self.stream[self.stream[self.pc + 2]]
            except:
                pass
            if code == 1: 
                self.stream[self.stream[self.pc + 3]] = va + vb
                self.pc += 4
            elif code == 2:
                self.stream[self.stream[self.pc + 3]] = va * vb
                self.pc += 4
            elif code == 3:
                self.stream[self.stream[self.pc + 1]] = self.inputs.pop(0)
                self.pc += 2
            elif code == 4:
                self.outVal = va
                self.pc += 2
                return (self.outVal, True)
            elif code == 5:
                if va != 0:
                    self.pc = vb 
                else:
                    self.pc += 3
            elif code == 6:
                if va == 0:
                    self.pc = vb 
                else:
                    self.pc += 3
            elif code == 7:
                self.stream[self.stream[self.pc + 3]] = 1 if va < vb else 0
                self.pc += 4
            elif code == 8:
                self.stream[self.stream[self.pc + 3]] = 1 if va == vb else 0
                self.pc += 4
            else:
                break
        return(self.outVal, False)

def runThrusters(stream,perm):
    machines = [machine(copy(stream),[perm[0],0]),
                machine(copy(stream),[perm[1]]),
                machine(copy(stream),[perm[2]]),
                machine(copy(stream),[perm[3]]),
                machine(copy(stream),[perm[4]])]

    outputs = [(0,True)] * 5
    outputs[0] = machines[0].runUntilOutput([])
    i = 1
    while outputs[4][1]:
        tmp = machines[i % 5].runUntilOutput(outputs[(i-1) % 5][0])
        outputs[i % 5] = tmp
        i += 1
    return outputs[4][0]


    
xs = [runThrusters(stream, x) for x in list(permutations(range(5)))]
print("PART1:", max(xs))
ys = [runThrusters(stream, x) for x in list(permutations(range(5,10)))]
print("PART2:", max(ys))
