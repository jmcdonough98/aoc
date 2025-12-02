import re

def testString(num):
    for l in range(1,len(num)):
        parts = [num[i:i+l] for i in range(0, len(num), l)]
        if all(part == parts[0] for part in parts):
            return len(num)//l
    return None

if __name__ == "__main__":
    name = "input.txt"
    f = open(name, 'r').read()
    p1c = 0
    p2c = 0
    for (a,b) in re.findall(r"(\d+)-(\d+)", f):
        for i in range(int(a), int(b) + 1):
            valid = testString(str(i))
            if valid is not None:
                p2c += i
            if valid == 2:
                p1c += i
    print(f"Part 1: {p1c}\nPart 2: {p2c}")
