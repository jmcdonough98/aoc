import math
WIDTH = 25
HEIGHT = 6
with open("input.txt","r") as f:
    line = f.read()
    layers = [line[i:i+(WIDTH*HEIGHT)] for i in range(0,len(line),WIDTH*HEIGHT)]

def getPart1(layers):
    minK = 0  
    minV = math.inf
    for k,v in enumerate(layers):
        a = v.count('0')
        if a < minV:
            minK = k
            minV = a
    return layers[minK].count('1') * layers[minK].count('2')

def constructMessage(layers):
    msg = WIDTH*HEIGHT*['2']
    for i in range(len(layers[0])):
        for j in range(len(layers)):
            if layers[j][i] != '2':
                msg[i] = layers[j][i]
                break
    return msg

print("PART1:",getPart1(layers))
tmp = ''.join(constructMessage(layers))

print("PART2:")
for k,v in enumerate(tmp):
    print(v,end=""),
    if (k+ 1) % WIDTH == 0:
        print()