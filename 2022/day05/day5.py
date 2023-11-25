from collections import defaultdict

def applyIns(boxes,ins):
    for (m,src,dst) in ins:
        tmp = boxes[src][-m:]
        boxes[src] = boxes[src][:-m]
        boxes[dst] += list(reversed(tmp))

    return "".join(boxes[i][-1] for i in range(1,len(boxes)+1))
def applyIns2(boxes,ins):
    for (m,src,dst) in ins:
        tmp = boxes[src][-m:]
        boxes[src] = boxes[src][:-m]
        boxes[dst] += tmp
    return "".join(boxes[i][-1] for i in range(1,len(boxes)+1))

def parseIns(txt):
    ins = []
    for line in txt.split('\n'):
        tmp = line.split(' ')
        ins.append((int(tmp[1]),int(tmp[3]),int(tmp[5])))
    return ins
def parseBoxes(txt):
    boxes = defaultdict(list)
    tmp = txt.split('\n')[:-1]
    N = len(tmp[0])//4 + 1
    for line in tmp:
        for i in range(N):

            if line[4*i+1] != ' ':
                boxes[i+1].append(line[4*i+1])
    for i in range(N):
        boxes[i+1] = list(reversed(boxes[i+1]))
    return boxes

def day5():
    s = open('input.txt','r').read().split('\n\n')
    p1boxes = parseBoxes(s[0])
    p2boxes = parseBoxes(s[0])
    ins = parseIns(s[1])
    print("Part 1:", applyIns(p1boxes, ins))
    print("Part 2:", applyIns2(p2boxes, ins))

if __name__ == "__main__":
    day5()