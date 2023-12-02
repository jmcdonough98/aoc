import re
s = open('input.txt','r').read().split('\n')

p1 = 0
p2 = 0
for i in range(len(s)):
    picks = s[i].split(': ')[1]
    valid = True
    mins = [0,0,0]
    for rnd in picks.split(';'):
        tmp = rnd.split(',')
        for t in tmp:
            val = int(re.search(r"(\d+)",t)[0])
            if "blue" in t:
                if val > 14:
                    valid = False
                mins[0] = max(mins[0], val)
            elif "red" in t:
                if val > 12:
                    valid = False
                mins[1] = max(mins[1], val)
            elif "green" in t:
                if val > 13:
                    valid = False
                mins[2] = max(mins[2], val)
    p2 += mins[0]*mins[1]*mins[2]
    if valid:
        p1 += i + 1

print("Part1:", p1)
print("Part2:", p2)