f = open("input")
ans1 = 0
ans2 = 0
def getFuelCount(n):
    fuel = 0
    while n // 3 - 2 > 0:
        fuel += (n // 3) - 2
        n //= 3
        n -= 2
    return fuel
for l in f:
    tmp = int(l)
    ans1 += (tmp // 3) - 2
    ans2 += getFuelCount(tmp)
    
print("Part 1:", ans1, " Part 2:",ans2)
