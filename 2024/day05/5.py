def shit_sort(x,ns, rules):
    invalid = True
    while invalid:
        invalid = False
        for r in rules:
            try:
                if ns[r[0]] > ns[r[1]]:
                    x[ns[r[0]]], x[ns[r[1]]] =  x[ns[r[1]]], x[ns[r[0]]]
                    ns[r[0]], ns[r[1]] = ns[r[1]], ns[r[0]]
                    invalid = True
            except:
                continue
    return int(x[len(x) // 2])

def day5(_input, rules):
    p1 = 0
    p2 = 0
    for l in _input:
        valid = True
        x = l.split(',')
        ns = {x[i]: i for i in range(len(x))}
        for r in rules:
            try:
                if ns[r[0]] > ns[r[1]]:
                    valid = False
            except:
                continue
        if valid:
            p1 += int(x[len(x) // 2])
        else:
            p2 += shit_sort(x,ns, rules)
    return p1, p2

if __name__ == "__main__":
    rules,_input = open('input.txt','r').read().split('\n\n')
    rules = [r.split('|') for r in rules.split('\n') ]
    _input = _input.split('\n')
    p1, p2 = day5(_input, rules)
    print("Part 1:", p1)
    print("Part 2:", p2)
