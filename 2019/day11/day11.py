from copy import copy
from collections import defaultdict
import matplotlib.pyplot as plt
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
    def enqueueInput(self,val):
        self.inputs.append(val)

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
                return (self.outVal,True)
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

class painter:
    def __init__(self,machine):
        self.coordColors = defaultdict(lambda: 0)
        self.m = machine
        self.dir = 0 # 0-up,1-right, 2 - down, 3-left
        self.x = 0
        self.y = 0

    def switchDir(self,n):
        self.dir = (self.dir + 1) % 4 if n else (self.dir - 1) % 4
    def move(self):
        if self.dir == 0:
            self.y += 1
        elif self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y -= 1
        elif self.dir == 3:
            self.x -= 1

    def paint(self):
        color,f1 = self.m.run()
        turn,f2 = self.m.run()
        if not (f1 and f2):
            return None #halted 
        self.coordColors[(self.x,self.y)] = color
        self.switchDir(turn)
        self.move()
        m.enqueueInput(self.coordColors[(self.x,self.y)])
        return 1

def part2(coords):
    pts = []
    for pt in coords:
        if coords[pt] == 1:
            pts.append(pt)
    x,y = zip(*pts)
    plt.scatter(x,y)
    plt.gcf().set_size_inches(6,1.3)
    plt.savefig("PART2.png")

m = machine(stream,[0])
p = painter(m)
while p.paint() != None:
    pass
print("PART1:",len(p.coordColors))

m = machine(stream,[1])
p = painter(m)
while p.paint() != None:
    pass
part2(p.coordColors)

print("PART2:", "IMAGE!")