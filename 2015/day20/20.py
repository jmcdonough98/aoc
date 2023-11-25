

def presentSeive(nmax):
    houses = [0] * (nmax + 1)
    for i in range(1,nmax + 1):
        for j in range(i,nmax + 1,i):
            houses[j] += 10*i
    for i in range(len(houses)):
        if houses[i] >= nmax:
            return i,houses[i]
def presentSeive2(nmax):
    houses = [0] * (nmax + 1)
    for i in range(1,nmax + 1):
        for j in range(1,51):
            try:
                houses[i*j] += 11*i
            except:
                break
    for i in range(len(houses)):
        if houses[i] >= nmax:
            return i,houses[i]
# print(presentSeive(10))
print(presentSeive2(33100000))