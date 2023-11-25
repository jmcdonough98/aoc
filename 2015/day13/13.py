from collections import defaultdict
from itertools import permutations
def parseInput():
    attitudes = defaultdict(lambda: defaultdict(int))
    peeps = set()
    with open('input.txt','r') as f:
        lines = f.read().split('\n')
    for l in lines:
        atoms = l.split(" ")
        sign = 1 if atoms[2] == 'gain' else -1
        attitudes[atoms[0]][atoms[-1][:-1]] = sign*int(atoms[3])
        peeps.add(atoms[0])
        # a = atoms[0]
        # b = atoms[-1]
    return attitudes,peeps

def optimalHappiness(attitudes,peeps):
    # print(attitudes['Alice']['Bob'])
    maxHap = 0
    for arr in permutations(peeps):
        hap = 0
        for i in range(len(arr) - 1):
            hap += attitudes[arr[i]][arr[i+1]]
            hap += attitudes[arr[i+1]][arr[i]]
        hap += attitudes[arr[0]][arr[-1]]
        hap += attitudes[arr[-1]][arr[0]]
        # print(hap)
        if hap > maxHap:
            maxHap = hap
    return maxHap
a,b = parseInput()
print("Part1", optimalHappiness(a,b))
b.add('me')
print("Part2",optimalHappiness(a,b))