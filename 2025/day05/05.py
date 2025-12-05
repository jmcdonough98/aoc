import re

def findFirst(a,b, ranges):
    for (c,d) in ranges:
        if a == c and b == d:
            continue
        if a <= c <= b or c <= a <= d:
            return (min(a,c), max(b,d))
        if a <= c <= b <= d:
            return (a,d)
        if c <= a <= d <= b:
            return (c,b)
    return (a,b)

def simplify(ranges):
    new = set()
    for (a,b) in ranges:
        new.add(findFirst(a,b,ranges))
    return new

if __name__ == "__main__":
    file = 'input.txt'
    ranges, ingreds = open(file, 'r').read().split('\n\n')
    ranges = [(int(x), int(y)) for (x,y) in re.findall(r"(\d+)-(\d+)", ranges)]
    ingreds = [int(x) for x in ingreds.split('\n')]

    while True: #simplify ranges until no change
        tmp = simplify(ranges)
        if len(ranges) == len(tmp):
            break
        ranges = tmp

    p1 = sum(any(x <= y <= z for (x,z) in ranges) for y in ingreds)
    p2 = sum(y - x + 1 for (x,y) in ranges)
    print(f"Part 1: {p1}\nPart 2: {p2}")
