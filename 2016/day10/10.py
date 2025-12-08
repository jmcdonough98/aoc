import re
from collections import defaultdict


def parse(file):
    lines = open(file).read().split('\n')
    bots = defaultdict(set)
    ins = []
    for l in lines:
        parse = re.findall(r"(bot \d+|output \d+|value \d+)", l)
        if l[0] == 'v': # assign chip
            bots[parse[1]].add(int(parse[0][6:]))
        if l[0] == 'b': # redistrib chips
            ins.append(parse)
    return bots, ins

def simulate(bots, ins):
    p1ans = None
    while True:
        for (src, low, high) in ins:
            if all(len(bots[x]) == 1 
                   for x in ['output 0', 'output 1','output 2']):
                return p1ans, bots['output 0'].pop()*bots['output 1'].pop()*bots['output 2'].pop()
            if len(bots[src]) < 2:
                continue
            if bots[src] == set([17, 61]):
                p1ans = src
            mi, ma = min(bots[src]), max(bots[src])
            bots[low].add(mi)
            bots[high].add(ma)
            bots[src].remove(mi)
            bots[src].remove(ma)

if __name__ == "__main__":
    file= 'input.txt'
    bots, ins = parse(file)
    p1, p2 = simulate(bots, ins)
    print(f"Part 1: {p1[4:]}\nPart 2: {p2}")