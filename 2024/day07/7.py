import re
from itertools import product

def checkValid(target, vals, ops):
    for opOrder in product(ops, repeat = len(vals) - 1):
        tmp = vals[0]
        for i in range(len(opOrder)):
            if opOrder[i] == "*":
                tmp *= vals[i+1]
            elif opOrder[i] == "+":
                tmp += vals[i+1]
            elif opOrder[i] == "":
                tmp = int(str(tmp) + str(vals[i+1]))
        if tmp == target:
            return True
    return False

def day7(_input):
    p1, p2 = 0,0
    for line in _input:
        target, *vals = [int(x) for x in re.findall(r"(\d+)", line)]
        if checkValid(target, vals, ["+","*"]):
            p1 += target 
            p2 += target
        elif checkValid(target, vals, ["+", "*",""]):
            p2 += target
    return p1, p2 
if __name__ == "__main__":

    _input = open('input.txt').read().split('\n')
    p1, p2 = day7(_input)
    print("Part 1:", p1)
    print("Part 2:", p2)
