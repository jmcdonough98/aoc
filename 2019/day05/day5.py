from copy import copy
with open("input.txt","r") as f:
    stream = [int(x) for x in f.read().split(",")]

def parseOpCode(n):
    codeVal = n % 100
    n //= 100
    modeA = n % 10
    n //= 10
    modeB = n % 10
    n //= 10
    modeC = n % 10 
    n //= 10
    return (codeVal,modeA,modeB,modeC)

def readCodes(stream,inVal):
    pCounter = 0
    outVals = []
    while pCounter < len(stream):
        (code,ma,mb,_) = parseOpCode(stream[pCounter])
        try:
            va = stream[pCounter + 1] if ma == 1 else stream[stream[pCounter + 1]]
            vb = stream[pCounter + 2] if mb == 1 else stream[stream[pCounter + 2]]
        except:
            pass
        if code == 1: 
            stream[stream[pCounter + 3]] = va + vb
            pCounter += 4
        elif code == 2:
            stream[stream[pCounter + 3]] = va * vb
            pCounter += 4
        elif code == 3:
            stream[stream[pCounter + 1]] = inVal
            pCounter += 2
        elif code == 4:
            outVals.append(va)
            pCounter += 2
        elif code == 5:
            if va != 0:
                pCounter = vb 
            else:
                pCounter += 3
        elif code == 6:
            if va == 0:
                pCounter = vb 
            else:
                pCounter += 3
        elif code == 7:
            stream[stream[pCounter + 3]] = 1 if va < vb else 0
            pCounter += 4
        elif code == 8:
            stream[stream[pCounter + 3]] = 1 if va == vb else 0
            pCounter += 4
        else:
            break
    return(outVals)

print("PART1:", readCodes(copy(stream),1)[-1])
print("PART2:", readCodes(copy(stream),5)[0])
