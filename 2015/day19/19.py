from collections import defaultdict
import time
def parseInput(s):
    tmp = s.split('\n\n')
    formulas = defaultdict(list)

    for l in tmp[0].split('\n'):
        left, right = l.split(' => ')
        formulas[left].append(right)
    return formulas, tmp[1]

def part1(formulas, inputMolecule):
    outputs = set()
    for i in range(len(inputMolecule)):
        if inputMolecule[i] in formulas:
            for output in formulas[inputMolecule[i]]:
                outputs.add(inputMolecule[:i] + output + inputMolecule[i+1:])
        tmp = inputMolecule[i:i+2]
        if tmp in formulas and len(tmp) == 2:
            for output in formulas[tmp]:
                outputs.add(inputMolecule[:i] + output + inputMolecule[i+2:])
    return outputs

def part2Stack(outs, backFormulas, inputMol):
    stack = ""
    

def part2(formulas,inputMol, target):
    outs = []
    backFormulas = {}
    for x in formulas:
        for y in formulas[x]:
            outs.append(y)
            backFormulas[y] = x
    outs = sorted(outs, key = lambda x: len(x),reverse=True)
    i = 1
    return part2Recursive(i, outs,backFormulas, inputMol)
    # while inputMol != 'e': #and i < 202:
    #     print(len(inputMol), inputMol)
    #     for o in outs:
    #         try:
    #             tmp = inputMol.index(o)
    #             inputMol = inputMol[:tmp] + backFormulas[o] + inputMol[tmp+len(o):]
    #             i += 1
    #             break
    #         except:
    #             continue
    # print(backFormulas)
    # print(i)
backtrack = set()
def part2Recursive(i,outs, backFormulas, inputMol):
    if i > 205:
        print(i)
    for o in outs:
        try:
            tmp = inputMol.index(o)
            modifiedMol = inputMol[:tmp] + backFormulas[o] + inputMol[tmp+len(o):]
            if modifiedMol == 'e':
                return i
            print(i, modifiedMol)
            
            if modifiedMol in backtrack:
                return None
            backtrack.add(modifiedMol)
            # time.sleep(0.1)
            tmp2 = part2Recursive(i+1,outs,backFormulas,modifiedMol)
            
            
            if tmp2 != None:
                return tmp2
        except:
            continue
    # backtrack.append(inputMol)
    return None

s = open('input.txt','r').read()
formulas, inputMolecule = parseInput(s)
# print("Part1:", len(part1(formulas,inputMolecule)))
print("Part2:", part2(formulas, inputMolecule, 'e'))
# print('abbbb'.index('bab'))
#195 = too low