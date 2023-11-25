lines = [int(x) for x in open('input.txt','r').read().split('\n')]

c = 0
for i in range(1,len(lines)):
    if lines[i] > lines[i-1]:
        c += 1 
l2 = [lines[i] + lines[i+1] + lines[i+2] for i in range(len(lines)-2)]

c2 = 0
for i in range(1,len(l2)):
    if l2[i] > l2[i-1]:
        c2 += 1 
print(c2)