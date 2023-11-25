from collections import defaultdict
lines = open('input.txt','r').read().split('\n')
fishies = [int(x) for x in lines[0].split(',')]
fishSticks = [0]*9
for f in fishies:
    fishSticks[f] += 1

def simDay(fishSticks):
    new = fishSticks[0]
    fishSticks[7] += new 
    fishSticks = fishSticks[1:] + [new]
    return fishSticks

P1, P2 = 80,256
for i in range(1, P2 + 1):
    fishSticks = simDay(fishSticks)
    if i == P1:
        print("P1:", sum(fishSticks))
print("P2:", sum(fishSticks))