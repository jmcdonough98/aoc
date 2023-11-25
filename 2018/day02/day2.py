from collections import defaultdict
def countLetters(code):
    counts = defaultdict(int)
    two = False
    three = False
    for c in code:
        counts[c] += 1
    for v in counts:
        if counts[v] == 2:
            two = True
        if counts[v] == 3:
            three = True
    return (two,three)
def part1():
    tmp = [countLetters(code) for code in codes]
    twothree = [0,0]
    for k,v in enumerate(tmp):
        if tmp[k][0]:
            twothree[0] += 1
        if tmp[k][1]:
            twothree[1] += 1
    return twothree[0]*twothree[1]
def strDiff(str1,str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count
def part2():
    for i in range(len(codes)):
        for j in range(i+1,len(codes)):
            if strDiff(codes[i],codes[j]) == 1:
                return (codes[i],codes[j])
f = open('input.txt','r')
codes = f.read().splitlines() 
print part1()
print part2()
