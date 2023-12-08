from math import lcm

def findPathLengths(currs):
    counts = [0]*len(currs)
    for j in range(len(currs)):
        i = 0
        stepCount = 0
        while True:
            if steps[i % len(steps)] == "R":
                currs[j] = Rs[currs[j]]
            else:
                currs[j] = Ls[currs[j]]
            stepCount += 1
            if currs[j][2] == "Z":
                break
            i += 1
        counts[j] = stepCount
    return lcm(*counts)
    
if __name__ == "__main__":
    ls = open('input.txt','r').read().split('\n')

    steps = ls[0]

    keys = ls[2:]
    Ls = {}
    Rs = {}
    for x in keys:
        k = x.split(' = ')[0]
        Ls[k] = x.split(' = ')[1][1:4]
        Rs[k] = x.split(' = ')[1][6:9]

    print("Part 1:", findPathLengths(["AAA"]))
    print("Part 2:", findPathLengths([x for x in Ls if x[2] == "A"]))
