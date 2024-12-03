
def tls(addr):
    hasAbba = False
    inBracket = False
    for i in range(len(addr)-3):
        tmp = addr[i:i+4]
        if tmp == tmp[::-1] and len(set(tmp)) != 1:
            if inBracket:
                return False
            hasAbba = True
        if addr[i] == '[':
            inBracket = True
        if addr[i] == ']':
            inBracket = False
    return hasAbba

def ssl(addr):
    abas = set()
    babs = set()
    inBracket = False
    for i in range(len(addr)-2):
        tmp = addr[i:i+3]
        if tmp == tmp[::-1] and len(set(tmp))!= 1:
            if inBracket:
                babs.add(tmp)
            else:
                abas.add(tmp)
        if addr[i] == '[':
            inBracket = True
        if addr[i] == ']':
            inBracket = False
    for aba in abas:
        if aba[1:] + aba[1] in babs:
            return True
    return False

def day7(_input):
    p1 = 0
    p2 = 0
    for line in _input:
        p1 += int(tls(line))
        p2 += int(ssl(line))
    return p1,p2



if __name__ == "__main__":
    _input = open('input.txt','r').read().split('\n')
    p1, p2 = day7(_input)
    print("Part 1:", p1)
    print("Part 2:", p2)