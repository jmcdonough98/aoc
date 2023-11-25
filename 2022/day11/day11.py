
class Monkey:
    def __init__(self, _id, items, worryRule, mod, t, f):
        self.id = _id
        self.items = items
        self.worryRule = worryRule
        self.mod = mod
        self.t = t
        self.f = f
        self.monkeyBusiness = 0
    def throw(self, x):
        return self.t if x % self.mod == 0 else self.f
    def updateWorry(self, old):
        return eval(self.worryRule)

def simulateRound(Monkeys,p1, N):
    for i in range(len(Monkeys)):
        for j in Monkeys[i].items:
            newWorry = Monkeys[i].updateWorry(j) // 3 if p1 else Monkeys[i].updateWorry(j) % N
            Monkeys[Monkeys[i].throw(newWorry)].items.append(newWorry)
            Monkeys[i].monkeyBusiness += 1
        Monkeys[i].items = []

    return Monkeys

def parseMonkeys():
    s = open('input.txt','r').read().split('\n\n')
    Monkeys = []
    for block in s:
        monkeyInfo = block.split('\n')
        monkeyID = int(monkeyInfo[0].split(' ')[1][:-1])
        monkeyItems = eval( "[" + monkeyInfo[1].split(":")[1] + "]")
        monkeyOp = monkeyInfo[2].split('=')[1]
    
        tMonkey = int(monkeyInfo[-2][-1])
        fMonkey = int(monkeyInfo[-1][-1])
        divVal = eval(monkeyInfo[3].split('by')[1])
        Monkeys.append(Monkey(monkeyID,monkeyItems,monkeyOp, divVal, tMonkey, fMonkey))

    return Monkeys

def run(numRounds, p1):
    Monkeys = parseMonkeys()
    N = 1
    for m in Monkeys:
        N *= m.mod
    for i in range(numRounds):
        Monkeys = simulateRound(Monkeys,p1, N)

    tmp = sorted([m.monkeyBusiness for m in Monkeys])
    return tmp[-1] * tmp[-2]

if __name__ == "__main__":
    print("Part 1:", run(20, True))
    print("Part 2:", run(10000, False))