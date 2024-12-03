
def p1(line):
    newline = ""
    i = 0
    while i < len(line):
        if line[i] == "(":
            i += 1
            tmp = ""
            while line[i] != ")":
                tmp += line[i]
                i += 1
            i += 1
            numChars, repeat = [int(x) for x in tmp.split('x')]
            
            newline += line[i:i+numChars] * repeat
            i += numChars
        else:
            newline += line[i]
            i += 1
    line = newline

    return len(newline)

def p2(line):
    ans = 0
    i = 0
    while i < len(line):
        if line[i] == "(":
            i += 1
            tmp = ""
            while line[i] != ")":
                tmp += line[i]
                i += 1
            i += 1
            numChars, repeat = [int(x) for x in tmp.split('x')]
            ans += repeat*p2(line[i:i+numChars])
            i += numChars
        else:
            ans += 1
            i += 1
    return ans

def day9(_input):
    a1,a2 = 0,0
    for line in _input:
        a1 += p1(line)
        a2 += p2(line)
    return a1, a2

if __name__ == "__main__":
    _input = open('input.txt','r').read().split('\n')
    a1,a2 = day9(_input)
    print("Part 1:", a1)
    print("Part 2:", a2)
