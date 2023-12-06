from math import sqrt, ceil,floor
from functools import reduce

def f(x):
    r1 = (x[0] - sqrt(x[0]**2 - 4*x[1])) / 2
    r2 = (x[0] + sqrt(x[0]**2 - 4*x[1])) / 2
    return floor(r2)-ceil(r1) - 1 if r2 - int(r2) == 0 else floor(r2)-ceil(r1) + 1

times, dists = open('input.txt', 'r').read().split('\n')
times = list(map(int, times.split(': ')[1].split()))
dists = list(map(int, dists.split(': ')[1].split()))

print("Part 1:", reduce(lambda x,y: x*y, map(f, zip(times, dists) )))
print("Part 2:", f((int("".join(str(x) for x in times)), int("".join(str(x) for x in dists)))))
