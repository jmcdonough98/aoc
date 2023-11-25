from itertools import permutations
import math
with open('input.txt') as f:
    lines = f.read().split('\n')
cities = set()
distances = {}
for l in lines:
    t = l.split(' ')
    cities.add(t[0])
    cities.add(t[2])
    distances[(t[0],t[2])] = int(t[4])
minDist = math.inf
maxDist = 0
for routes in permutations(cities):
    d = 0
    for i in range(1,len(routes)):
        try:
            d+= distances[(routes[i],routes[i-1])]
        except:
            d+= distances[(routes[i-1],routes[i])]
    if d < minDist:
        minDist = d
    if d > maxDist:
        maxDist = d


print('PART1:',minDist,'\nPART2:',maxDist)
