with open('input.txt') as f:
    strings = f.read().split('\n')
print('PART1', sum([len(s) - len(eval(s)) for s in strings]))
print('PART2', sum([len(repr(s)) + s.count('\"') - len(s) for s in strings])) #repr doesn't escape double quotes