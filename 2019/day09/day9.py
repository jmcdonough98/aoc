from itertools import permutations
from copy import copy
with open("input.txt","r") as f:
    stream = [int(x) for x in f.read().split(",")]

class machine:
    def __init__(self,s,inputs= [],pc = 0, relBase = 0):
        self.stream = s + 500*[0] #provide extra memory
        self.inputs = inputs 
        self.pc = pc
        self.outVal = 0
        self.relBase = relBase

    def parseOpCode(self,n):
        codeVal = n % 100
        n //= 100
        modeA = n % 10
        n //= 10
        modeB = n % 10
        n //= 10
        modeC = n % 10 
        n //= 10
        return (codeVal,modeA,modeB,modeC)

    def chooseMode(self,mode,offset):
        if mode == 0:
            return self.stream[self.pc + offset]
        if mode == 1:
            return self.pc + offset
        if mode == 2: 
            return self.stream[self.pc + offset] + self.relBase

    def run(self,newInput = []):
        if newInput != []:
            self.inputs.append(newInput)
        while self.pc < len(self.stream):
            (code,ma,mb,mc) = self.parseOpCode(self.stream[self.pc])
            try:
                posA = self.chooseMode(ma,1)
                posB = self.chooseMode(mb,2)
                posC = self.chooseMode(mc,3)
            except:
                pass
            if code == 1: 
                self.stream[posC] = self.stream[posA] + self.stream[posB]
                self.pc += 4
            elif code == 2:
                self.stream[posC] = self.stream[posA] * self.stream[posB]
                self.pc += 4
            elif code == 3:
                self.stream[posA] = self.inputs.pop(0)
                self.pc += 2
            elif code == 4:
                self.outVal = self.stream[posA]
                self.pc += 2
                return self.outVal
            elif code == 5:
                if self.stream[posA] != 0:
                    self.pc = self.stream[posB]
                else:
                    self.pc += 3
            elif code == 6:
                if self.stream[posA] == 0:
                    self.pc = self.stream[posB]
                else:
                    self.pc += 3
            elif code == 7:
                self.stream[posC] = 1 if self.stream[posA] < self.stream[posB] else 0
                self.pc += 4
            elif code == 8:
                self.stream[posC] = 1 if self.stream[posA] == self.stream[posB] else 0
                self.pc += 4
            elif code == 9:
                self.relBase += self.stream[posA]
                self.pc += 2
            else:
                break
        return(self.outVal, False)

m = machine(copy(stream),inputs=[1])
print("PART 1:",m.run())
m = machine(copy(stream),inputs=[2])
print("PART 2:",m.run())

