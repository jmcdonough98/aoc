# Find the leftmost maximum of bank, M at index i
# split bank into bank[:i], bank[i+1:]
# run algorithm on bank[i+1:]
# if 1 + len(output) == desired output, stop
# else run the algorithm on the left to get the remaining digits

def maximizeJoltage(bank, digits):
    if len(bank) == 0 or digits <= 0:
        return []
    m, idx = 0, None
    for i in range(len(bank)):
        if int(bank[i]) > m:
            m = int(bank[i])
            idx = i
    left = bank[:idx]
    right = bank[idx+1:]
    res = maximizeJoltage(right, digits-1)
    if len(res) == digits - 1:
        return [m] + res
    return maximizeJoltage(left, digits - len(res) - 1) + [m] + res

def helper(li):
    return int("".join(str(x) for x in li))

filename = 'input.txt'
lines = open(filename, 'r').read().split('\n')

p1c = 0
p2c = 0
for bank in lines:
    p1c += helper(maximizeJoltage(bank, 2))
    p2c += helper(maximizeJoltage(bank, 12))
print(f"Part 1: {p1c}\nPart 2: {p2c}")