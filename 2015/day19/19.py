import re
from collections import Counter
lines = open('input.txt','r').read().split('\n')

rules = [x.split(' => ') for x in lines[:-2]]
molecule = lines[-1]


def applyrule(molecule, idx, old, new):
    return molecule[:idx] + new + molecule[idx+len(old):]

def part1(rules, molecule):
    newMolecules = set()
    for (old, new) in rules:
        for i in range(len(molecule)):
            if molecule[i:i+len(old)] == old:
                newMolecules.add(applyrule(molecule, i,old, new))
    return len(newMolecules)


def part2(molecule):
    molecule = re.sub(r"O|P|B|Mg|Ca|Si|Th|F|B|Al|Ti|C|H", "A", molecule)
    molecule = re.sub(r"Rn|Ar", "B", molecule)
    molecule = re.sub(r"Y", "C", molecule)
    c = Counter(molecule)
    return len(molecule) - c["B"] - 2*c["C"] - 1

print(part1(rules, molecule))
print(part2(molecule))



