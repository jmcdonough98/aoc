def iterate(seq,nmax):
    initLen = len(seq)
    lastSeen = {}
    for i in range(initLen - 1):
        lastSeen[seq[i]] = i 
    for i in range(initLen,nmax):
        lastSpoken = seq[-1]
        if lastSpoken not in lastSeen:
            seq.append(0)
        elif lastSeen[lastSpoken] < i - 1:
            new = i - lastSeen[lastSpoken] - 1
            seq.append(new)
        else:

            seq.append(0)
        lastSeen[seq[i-1]] = i - 1
    return seq[-1]

print(iterate([0,13,16,17,1,10,6],2020))
print(iterate([0,13,16,17,1,10,6],30000000))
