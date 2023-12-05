import re

s = open('input.txt','r').read().split('\n\n')
seeds = list(map(int, re.findall(r"(\d+)", s[0][5:])))
seedIntervals = [(seeds[2*i], seeds[2*i] + seeds[2*i + 1] - 1) for i in range(len(seeds) // 2)]

for l in s[1:]:
    tmp = l.split('\n')
    srcs = []
    dsts = []
    rngs = []
    for vals in tmp[1:]:
        dst, src, rng = list(map(int, re.findall(r"(\d+)", vals)))
        dsts.append(dst)
        srcs.append(src)
        rngs.append(rng)
    
    for j in range(len(seeds)):
        for i in range(len(srcs)):
            if srcs[i] <= seeds[j] <= srcs[i] + rngs[i] - 1:
                seeds[j] = dsts[i] + (seeds[j] - srcs[i])
                break

    newSeedIntervals = []
    while len(seedIntervals) > 0: # evaluate intervals, splitting as necessary
        curr = seedIntervals.pop()
        if curr[0] > curr[1]:
            continue
        modified = False 
        for i in range(len(srcs)):
            if srcs[i] <= curr[0] <= curr[1] <= srcs[i] + rngs[i] - 1: # whole interval gets mapped
                newSeedIntervals.append((curr[0] + dsts[i] - srcs[i], curr[1] + dsts[i] - srcs[i]))
                modified = True
                break
            elif curr[0] < srcs[i] <= srcs[i] + rngs[i] - 1 < curr[1]: #interval split
                seedIntervals.append((curr[0], srcs[i] - 1))
                seedIntervals.append((srcs[i] + rngs[i], curr[1]))
                newSeedIntervals.append((dsts[i], dsts[i] + rngs[i] - 1))
                modified = True
                break
            elif srcs[i] <= curr[0] <= srcs[i] + rngs[i] - 1 <= curr[1]: #start of interval gets mapped
                newSeedIntervals.append((curr[0] + dsts[i] - srcs[i], dsts[i] + rngs[i] - 1))
                seedIntervals.append((srcs[i] + rngs[i], curr[1]))
                modified = True
                break
            elif curr[0] <= srcs[i] <= curr[1] <= srcs[i] + rngs[i] - 1: #end of interval gets mapped
                newSeedIntervals.append((dsts[i], curr[1] + dsts[i] - srcs[i]))
                seedIntervals.append((curr[0], srcs[i] - 1))
                modified = True
                break 
        if not modified: #completely disjoint, move it along
            newSeedIntervals.append(curr)
    seedIntervals = newSeedIntervals

print("Part 1:", min(seeds))
print("Part 2:", min(seedIntervals, key = lambda x: x[0])[0])
