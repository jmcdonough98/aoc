from collections import defaultdict

def parseHand(h):
    cVals = {"A":14, "K":13, "Q":12, "J":11, "T":10}
    scoreCard = lambda x: cVals[x] if x in cVals else int(x)
    tal = defaultdict(int)
    for i in range(5):
        tal[scoreCard(h[i])] += 1
    return ([scoreCard(x) for x in h[:5]], sorted(tal.values(), reverse = True), int(h[6:]))

def parseHand2(h):
    cVals = {"A":14, "K":13, "Q":12, "J":1, "T":10}
    scoreCard = lambda x: cVals[x] if x in cVals else int(x)
    tal = defaultdict(int)
    for i in range(5):
        tal[scoreCard(h[i])] += 1
    jokerCount = 0
    if 1 in tal:
        jokerCount = tal[1]
        del tal[1]
    tmpVals = sorted(tal.values(), reverse = True)
    try:
        tmpVals[0] += jokerCount
    except:
        tmpVals = [jokerCount] # very funny, Eric...
    return ([scoreCard(x) for x in h[:5]], tmpVals, int(h[6:]))

def lazysort(s):
    def le(h1,h2):
        if h1[1] == h2[1]: # hand pattern
            return h1[0] < h2[0] # lex order on card values if same hand pattern.
        return h1[1] < h2[1]
    # insertion sort, don't need (rather, can't be bothered) something more efficient...
    for i in range(len(s)):
        x = s[i]
        j = i - 1
        while j >= 0 and  le(x, s[j]):
            s[j+1] = s[j]
            j -= 1
        s[j+1] = x
    return s

    

if __name__ == "__main__":
    s = open('input.txt','r').read().split('\n')

    hands = lazysort([parseHand(x) for x in s])
    print("Part 1:", sum(hands[i][2]*(i+1) for i in range(len(hands)) ))

    hands2 = lazysort([parseHand2(x) for x in s])
    print("Part 2:", sum(hands2[i][2]*(i+1) for i in range(len(hands2)) ))
