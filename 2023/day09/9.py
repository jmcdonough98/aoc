


def calculuateNextTerm(l):
    depth = 0
    derivatives = [l]
    while any(x != 0  for x in derivatives[-1]):
        derivatives.append([
            derivatives[-1][i+1] - derivatives[-1][i] for i in range(len(derivatives[-1]) - 1)
        ])
    
    for i in range(len(derivatives)-2, -1, -1):
        derivatives[i].append(derivatives[i][-1] + derivatives[i+1][-1])
        derivatives[i].insert(0, derivatives[i][0] - derivatives[i+1][0])
    return (derivatives[0][0], derivatives[0][-1])


ls = ([int(x) for x in l.split()] for l in open('input.txt','r').read().split('\n'))
ans = [calculuateNextTerm(x) for x in ls]
print("Part 1:", sum(x[1] for x in ans))
print("Part 2:", sum(x[0] for x in ans))