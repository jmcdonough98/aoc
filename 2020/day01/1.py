with open('input.txt','r') as f:
    s = [int(x) for x in f.read().split('\n')]

def part_1(s):
    for x in s:
        for y in s:
            if x + y == 2020:
                return(x*y)
def part_2(s):
    for x in s:
        for y in s:
            for z in s:
                if x + y + z== 2020:
                    return(x*y*z)
print("PART1:",part_1(s))
print("PART2:",part_2(s))