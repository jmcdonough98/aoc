from collections import defaultdict

def day6(lines):
    N = len(lines[0])
    cols = [defaultdict(int) for i in range(N)]
    for line in lines:
        for i in range(len(line)):
            cols[i][line[i]] += 1
    p1 = ""
    p2 = ""
    for c in cols:
        p1 += max(c, key = lambda x: c[x])
        p2 += min(c, key = lambda x: c[x])
    return "".join(p1), "".join(p2)

if __name__ == "__main__":
    lines = open('input.txt','r').read().split('\n')
    p1, p2 = day6(lines)
    print("Part 1:", p1)
    print("Part 2:", p2)