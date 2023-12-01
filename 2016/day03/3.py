import re 

def part2():
    valid = lambda x, y, z: int(x + y > z and x + z > y and y + z > x)
    entries = []
    for l in s:
        entries.append(list(map(int, re.findall(r"(\d+)", l))))

    c = 0
    for i in range(0, len(entries), 3):
        c += valid(entries[i][0], entries[i+1][0],entries[i+2][0]) + \
            valid(entries[i][1], entries[i+1][1],entries[i+2][1]) + \
            valid(entries[i][2], entries[i+1][2],entries[i+2][2])
    return c

if __name__ == "__main__":
    s = open('input.txt','r').read().split('\n')
    
    print("Part 1:", sum(all(x[i] + x[(i+1)%3] > x[(i+2)%3] for i in range(3)) for x in map(lambda l: list(map(int, re.findall(r"(\d+)", l))), s)))
    print("Part 2:", part2())