filename = "input.txt"
lines = open(filename, 'r').read().split('\n')
p1_c = 0
p2_c = 0
sd = {"L":-1, "R":1}
dial = 50
for ins in lines:
    LR = ins[0]
    val = int(ins[1:])
    p2_c += val // 100
    val %= 100
    new_dial = dial + sd[LR]*val
    if (new_dial < 0 and dial != 0) or new_dial > 100:
        p2_c += 1
    dial = new_dial % 100
    if dial == 0:
        p1_c += 1
        p2_c += 1

print(f"Part 1: {p1_c}\nPart 2: {p2_c}")