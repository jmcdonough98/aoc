

ing = [(2,0,-2,0,3),(0,5,-3,0,3),(0,0,5,-1,8),(0,-1,0,5,8)]
test = [(-1,-2,6,3,8),(2,3,-2,-1,3)]

def scoreCookie(ings, split, flag = 1):
    score = 1
    for i in range(len(ings[0]) - 1):
        tmp = sum([split[x]*ings[x][i] for x in range(len(split))])
        if tmp <= 0:
            return 0
        score *= tmp
    if flag == 1:
        calories = sum([split[x]*ings[x][-1] for x in range(len(split))])
        if calories != 500:
            return 0
    return score

#you could definitely do this with some kind of memoized algorithm, it wouldn't be that much more efficient though I think.
def findOptimalArrangment(N,countCalories = 0):
    maxScore = -1
    for x in range(1,N+1):
        for y in range(1,N-x):
            for z in range(1,N-x-y):
                w = N - z - y - x
                score = scoreCookie(ing,[x,y,z,w],countCalories)
                if score > maxScore:
                    maxScore = score
    return maxScore
def findOptimalArrangmentTest(N):
    maxScore = -1
    for x in range(1,N + 1):
        y = N-x
        score = scoreCookie(test,[x,y],0)
        if score > maxScore:
            maxScore = score

    return maxScore

print(findOptimalArrangment(100))
print(findOptimalArrangment(100,1))