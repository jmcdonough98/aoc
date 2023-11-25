import numpy as np #easy 16bit ints
from collections import defaultdict

#### OPS
# bitwise AND 0
# bitwise OR 1 
# bitwise NOT 2
# left shift 3 
# right shift 4
# assignment 5
def isInt(s):
    try:
        int(s)
        return True
    except:
        return False

def parseInstructions(filename):
    binops = {'AND':0, 'OR':1, 'LSHIFT':3, 'RSHIFT':4}
    

    with open(filename) as f:
        instructions = f.read().split('\n')
    parsedIns = {}
    dependencyGraph = defaultdict(list)
    for ins in instructions:
        parts = ins.split(' ')
        #assignment
        if len(parts) == 3:
            if isInt(parts[0]):
                x = int(parts[0])
            else:
                x = parts[0]
                dependencyGraph[x].append(parts[-1])
            parsedIns[parts[-1]] = (5, [x])
        #negation
        elif len(parts) == 4:
            if isInt(parts[1]):
                x = int(parts[1])
            else:
                x = parts[1]
                dependencyGraph[x].append(parts[-1])
            parsedIns[parts[-1]] = (2, [x])
        #binary op, parts[1] tells us which one
        elif len(parts) == 5:
            if isInt(parts[0]):
                x = int(parts[0])
            else:
                x = parts[0]
                dependencyGraph[x].append(parts[-1])
            if isInt(parts[2]):
                y = int(parts[2])
            else:
                y = parts[2]
                dependencyGraph[y].append(parts[-1])
            parsedIns[parts[-1]] = (binops[parts[1]], [x,y])

    return parsedIns, dependencyGraph

def toposort(graph):
    seen = set()
    stack = []
    order = []
    q = list(graph.keys())
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v)
            q.extend(graph[v])
            while stack and v not in graph[stack[-1]]:
                order.append(stack.pop())
            stack.append(v)
    return stack + order[::-1]

def evaluateCircuit(instructions,order):
    wires = defaultdict(np.uint16)
    

    for wire in order:
        op, args = instructions[wire]
        for i in range(len(args)):
            if not isInt(args[i]):
                args[i] = np.uint16(wires[args[i]])
        if op == 0:
            wires[wire] = np.uint16(args[0] & args[1])
        elif op == 1:
            wires[wire] = np.uint16(args[0] | args[1])
        elif op == 2:
            wires[wire] = ~np.uint16(args[0])
        elif op == 3:
            wires[wire] = np.uint16(args[0] << args[1])
        elif op == 4:
            wires[wire] = np.uint16(args[0] >> args[1])
        elif op == 5:
            wires[wire] = np.uint16(args[0])
    return wires['a']


instructions,dependencyGraph = parseInstructions('input.txt')
order = toposort(dependencyGraph)
print('PART1:',evaluateCircuit(instructions,order))
i2,d2 = parseInstructions('input2.txt') #replaced b code as described in problem
print('PART2:',evaluateCircuit(i2,order))
