sizes = sorted([11,30,47,31,32,36,3,1,5,3,32,36,15,11,46,26,28,1,19,3])[::-1]
tsizes = [20,15,10,5,5]

numContainers = []
def recursiveCounter(n,sizes, count,depth):
    count = 0
    if sizes == []:
        return 0
    for i,s in enumerate(sizes):
        if n - s == 0:
            #valid arrangement of containers found, keep track of the depth for part 2
            numContainers.append(depth+1)
            count+= 1
        if n - s < 0:
            continue
        if n - s > 0:
            count += recursiveCounter(n-s,sizes[i+1:],count,depth+1)
    return count

print(recursiveCounter(150,sizes,0,0))
print(numContainers.count(min(numContainers)))