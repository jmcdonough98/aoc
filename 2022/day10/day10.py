s = open('input.txt','r').read().split('\n')

cycleTime = {
    "noop":1,
    "addx":2
}

cnt = 0

targets = [20,60,100,140,180,220]
cycleCount = 0
regVal = 1
i = 0
print("Part 2:")
for line in s:
    if cycleCount + 2 in targets:
        cnt += regVal*(cycleCount + 2)
        targets.remove(cycleCount + 2)
    if cycleCount + 1 in targets:
        cnt += regVal*(cycleCount + 1)
        targets.remove(cycleCount + 1)
    cycleCount += cycleTime[line[:4]]
    while i < cycleCount:
        if abs((i % 40) - regVal) <= 1:
            print("#",end='')
        else:
            print(".",end='')
        i += 1
        if i % 40 == 0:
            print()
    regVal = regVal if line[:4] == "noop" else regVal + int(line[5:])
print("Part 1:",cnt)
