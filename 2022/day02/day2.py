_input = open('input.txt','r').read().split('\n')
encodeInput = lambda s: (ord(s[0]) - ord('A'), ord(s[2]) - ord('X'))
# mod 3, c[1] - c[0] + 1 is 0 when you lose, 1 when you draw, and 2 when you win.
guide1 = lambda c: ((c[1] - c[0] + 1) % 3) * 3 + (c[1] + 1)
# given a state c[1] and an opponent move c[0], your move is given by the solution to the equation c[0] - x = c[1] + 1 mod 3
guide2 = lambda c: c[1]*3 + (c[0] + c[1] - 1) % 3 + 1
print("Part 1:", sum(map(guide1, map(encodeInput, _input))))
print("Part 2:", sum(map(guide2, map(encodeInput, _input))))

print((lambda g1,g2, d: (sum(map(g1,d)), sum(map(g2,d))))(lambda c: ((c[1] - c[0] + 1) % 3) * 3 + (c[1] + 1), lambda c: c[1]*3 + ((c[0] + c[1] - 1) % 3) + 1, list(map(lambda s: (ord(s[0]) - ord('A'), ord(s[2]) - ord('X')), open('input.txt','r').read().split('\n')))))

