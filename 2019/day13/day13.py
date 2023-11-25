with open("input.txt","r") as f:
    stream = [int(x) for x in f.read().split(",")]
import os
HEIGHT = 23 + 1
WIDTH = 36 + 1
# 0 = empty " "
# 1 = wall "X"
# 2 = block "B"
# 3 = paddle "="
# 4 = ball "O"
displayKeys = {0:' ', 1:'X',2:'B',3:'_',4:'O'}
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

class cabinet:
    def __init__(self,stream,mode = 1):
        self.screen = [[" " for i in range(WIDTH)] for j in range(HEIGHT)]
        stream[0] = mode
        self.m = machine(stream)
        self.initDisplay()
        self.score = 0
        self.blockCount = self.partOne()
        self.ball = []
        self.paddle = []

    def partOne(self):
        c = 0
        for line in self.screen:
            for char in line:
                if char == "B":
                    c += 1
        return c
    def initDisplay(self):
        for _ in range(WIDTH):
            for _ in range(HEIGHT):
                x,_ = self.m.run()
                y,_ = self.m.run()
                val,_ = self.m.run()
                self.screen[y][x] = displayKeys[val]
    def display(self):
        print("Score:",self.score)
        for i in range(len(self.screen)):
            for j in range(len(self.screen[i])):
                print(self.screen[i][j],end="")
            print()
    def runGame(self):
        f1 = f2 = f3 = True
        self.m.enqueueInput(-1)
        while f1 and f2 and f3:
            try:
                x, f1   = self.m.run()
                y, f2   = self.m.run()
                val, f3 = self.m.run()
            except:
                pass
            if x == -1 and y == 0:
                self.score = val
                # print("score updated",self.score)
            else:
                if val == 3: # paddle moved
                    self.paddle = [x,y]
                if val == 4:
                    # ball moved
                    self.ball = [x,y]
                    if self.ball[0] > self.paddle[0]:
                        self.m.enqueueInput(1)
                    elif self.ball[0] < self.paddle[0]:
                        self.m.enqueueInput(-1)
                    else:
                        self.m.enqueueInput(0)
                try:
                    self.screen[y][x] = displayKeys[val]
                    # os.system('cls')
                    # self.display()
                except:
                    return val

c = cabinet(stream,mode = 2)
print("Part 1:",c.blockCount)
print("PART 2:",c.runGame())