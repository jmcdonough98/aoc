twos = [str(i)*2 for i in range(10)]
threes = [str(i)*3 for i in range(10)]  
def findSpecialNums(a,b,p1=True):
    c = 0
    for i in range(a, b+1):
        if testOneNum(i,p1):
            c+=1
    return c 

def testOneNum(n,p1):
    x = str(n)
    special = False
    for i in range(10):
        if twos[i] in x and (threes[i] not in x or p1):
            special = True
    for j in range(1,len(x)):
        if int(x[j]) < int(x[j-1]):
            special = False
            break

    return special
print("PART1: ", findSpecialNums(307237,769058))
print("PART2: ", findSpecialNums(307237,769058,p1 = False))