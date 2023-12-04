
import re
s = open('input.txt','r').read().split('\n')

totalScore = 0
copies = [1]*len(s)

for i,l in enumerate(s):
    info = l.split(": ")[1].split(' | ')
    winningNums = [int(x) for x in re.findall(r"(\d+)", info[0])]
    scratchNums = [int(x) for x in re.findall(r"(\d+)", info[1])]
    c = 0
    for n in winningNums:
        if n in scratchNums:
            c += 1
    
    if c != 0:
        totalScore += 2**(c-1)
        for j in range(i+1,i+c+1):
            copies[j] += copies[i]
print(totalScore, sum(copies))