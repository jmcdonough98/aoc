from collections import defaultdict
from functools import reduce

isVowel = lambda c: c in "aeiou"
bad = lambda cc: cc in ["ab","cd","pq","xy"]

def hasBadSubString(s):
    for i in range(len(s)):
        if bad(s[i:i+2]):
            return True
    return False
    
def threeVowels(s):
    count = 0
    for c in s:
        if isVowel(c):
            count+= 1
        if count == 3:
            return True
    return False

def hasDouble(s):
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            return True
    return False

def hasDisjointPair(s):
    pairCount = defaultdict(int)
    pairIndex = defaultdict(list)
    for i in range(len(s)):
        tmp = s[i:i+2]
        pairCount[tmp] += 1
        pairIndex[tmp].append(i)
    # print(pairCount,pairIndex)
    for pair in pairCount:
        if pairCount[pair] > 1:
            #input has no    
            diffs =  [(y-x) > 1 for x,y in zip(pairIndex[pair], pairIndex[pair][1:])]

 
            if reduce(lambda x,y: x and y,diffs):
                return True
    return False
        

def hasPalindromeTriple(s):
    for i in range(len(s) - 2):
        tmp = s[i:i+3]
        if tmp[0] == tmp[2]:
            return True
    return False

def solve():
    with open('input.txt') as f:
        strings = f.read().split('\n')

    wc1 = 0
    for s in strings:
        if threeVowels(s) and (not hasBadSubString(s)) and hasDouble(s):
            wc1 += 1
    wc2 = 0
    for s in strings:
        if hasPalindromeTriple(s) and hasDisjointPair(s):
            wc2+=1
    print('Part 1:', wc1)
    print('Part 2:', wc2)
solve()
# print(hasPalindromeTriple('xywxaab'))
# print(hasDisjointPair('aaa'))