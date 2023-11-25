import re
_input = open('input.txt','r').read()

parsedInput = [list(map(int, x)) for x in re.findall(r"(\d+)-(\d+),(\d+)-(\d+)",_input)]

counter1 = 0
counter2 = 0
for pair in parsedInput:
    if (pair[2] >= pair[0] and pair[3] <= pair[1]) or\
        (pair[2] <= pair[0] and pair[3] >= pair[1]):
        counter1 += 1
    elif (pair[2] <= pair[1] <= pair[3]) or (pair[2] <= pair[0] <= pair[3]):
        counter2 += 1

print("Part 1:", counter1)
print("Part 2:", counter2 + counter1)