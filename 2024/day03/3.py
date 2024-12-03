import re

def day3(mem):
    parseMem = lambda mem: sum(int(x)*int(y) for (x,y) in re.findall(r"mul\((\d+),(\d+)\)", mem))
    p1 =  parseMem(mem)
    p2 = 0

    for i,x in enumerate(mem.split("don't()")):
        if i == 0:
            p2 += sum(parseMem(y) for y in x.split('do()'))
        else:
            p2 += sum([parseMem(y) for y in x.split('do()')[1:]])
    return p1, p2

if __name__ == "__main__":
    mem = open('input.txt','r').read()
    p1,p2 = day3(mem)
    print("Part 1:", p1)
    print("Part 2:", p2)