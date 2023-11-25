data = [int(d) for d in open('input.txt','r').read().split(" ")]

def traverseTreeOne():
    def traverseNode(i):
        branchSum = 0
        while data[i] != 0:
            branchSum += traverseNode(i+2)
            data[i] -= 1
        m = data[i+1]
        metadata = data[i+2:i+2+m]
        data[i:i+2+m] = []
        branchSum += sum(metadata)
        return branchSum
    return traverseNode(0)

def traverseTreeTwo():
    def traverseNode(i):
        if data[i] == 0: #child node
            m = data[i+1]
            metadata = data[i+2:i+2+m]
            data[i:i+2+m] = []
            return sum(metadata)
        nodeSum = 0
        childSums = []
        while data[i] != 0:
            childSums.append(traverseNode(i+2))
            data[i] -= 1
        m = data[i+1]
        metadata = data[i+2:i+2+m]
        data[i:i+2+m] = []
        for md in metadata:
            if md - 1 in range(0,len(childSums)):
                nodeSum += childSums[md - 1]
        
        return nodeSum
    return traverseNode(0)

#print traverseTreeOne()
print traverseTreeTwo()
