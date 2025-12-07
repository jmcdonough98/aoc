def flip(A):
    return ["".join(x) for x in zip(*A)]

file = 'input.txt'
lines = open(file).read().split('\n')
sp = [i for i in range(len(lines[-1])) if lines[-1][i] in ['+','*']] + [len(lines[-1]) + 1]

p1c = 0
p2c = 0
for i in range(len(sp)-1):
    op = lines[-1][sp[i]]
    p1c += eval("".join(lines[j][sp[i]:sp[i+1]-1] + op for j in range(len(lines) - 1))[:-1])
    p2c += eval("".join(x + op for x in flip(list(lines[j][sp[i]:sp[i+1]-1]) for j in range(len(lines) - 1)))[:-1])

print(f"Part 1: {p1c}\nPart 2: {p2c}")