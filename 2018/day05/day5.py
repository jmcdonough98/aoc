from string import ascii_lowercase
test = "dabAcCaCBAcCcaDA"
polymer = open('input.txt','r').read()

def shortenPolymer(s):
    changed = True
    while changed:
        changed = False
        for i in range(len(s)-2):
            if i >= len(s) - 1:
                break
            if ord(s[i]) ^ ord(s[i+1]) == 32:
                s = s[:i] + s[i+2:]
                changed = True
    return len(s)
    
minLen = len(polymer)
for c  in ascii_lowercase:
    newLen = shortenPolymer(polymer.replace(c,"").replace(c.upper(),""))
    if  newLen < minLen:
        minLen = newLen
print "Part 1: " + str(shortenPolymer(polymer))
print "Part 2: " + str(minLen)
