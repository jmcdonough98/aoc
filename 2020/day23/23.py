def createCups(string,numCups):
    A = [None]*(numCups + 1)
    tmp = [int(x) for x in string]
    for i in range(len(tmp)):
        A[tmp[i]] = (tmp[i], tmp[(i-1)%len(tmp)],tmp[(i+1)%len(tmp)])
    if numCups != len(tmp):
        A[tmp[-1]] = (A[tmp[-1]][0],A[tmp[-1]][1],len(tmp) + 1 ) 
        A[len(tmp) + 1] =  (len(tmp) + 1, tmp[-1], len(tmp) + 2)
        for i in range(len(tmp) + 2, numCups):
            A[i] = (i, i-1,i+1)
        A[numCups] = (numCups, numCups - 1, tmp[0])
        A[tmp[0]] = (A[tmp[0]][0], numCups, A[tmp[0]][2] )
    return A

def simulateGame(cups,currVal, turns = 1):
    for i in range(turns):
        currCup = cups[currVal]
        pickup = [cups[currCup[2]]]
        for j in range(2):
            pickup.append(cups[pickup[-1][2]])
        pickupVals = [x[0] for x in pickup]
        startCup,endCup = pickup[0],pickup[2]
        startVal,endVal = pickupVals[0],pickupVals[2]
        dstVal = (currVal - 1) if currVal != 1 else len(cups) - 1
        while dstVal in pickupVals:
            dstVal = (dstVal - 1) if dstVal != 1 else len(cups) -1 
        dstCup = cups[dstVal]

        #remove the 3 cups
        cups[currVal] = (currVal,currCup[1], endCup[2])
        cups[endCup[2]] = (cups[endCup[2]][0], currVal, cups[endCup[2]][2])
        tmp = cups[dstCup[2]]
        #connect tail of dst to head of pickedup
        cups[dstVal] = (dstCup[0],dstCup[1],startVal)
        cups[startVal] = (startCup[0],dstVal, startCup[2])
        # connect tail of pickedup to head of after dst
        cups[tmp[0]] = (tmp[0], endVal, tmp[2])
        cups[endVal] = (endVal, endCup[1], tmp[0])
        # print(currCup)
        currVal = cups[currVal][2]

def p1Score(cups):
    ans = ""
    x = cups[cups[1][2]]
    while x[0] != 1:
        ans += str(x[0])
        x = cups[x[2]]
    return ans
def p2Score(cups):
    n1 = cups[1][2]
    n2 = cups[n1][2]
    return n1*n2

_in = "523764819"
start = int(_in[0])
cups = createCups(_in,9)
simulateGame(cups,start,100)
print("Part 1", p1Score(cups))
cups = createCups(_in,1000000)
simulateGame(cups,start,10000000)
print("Part 2", p2Score(cups))