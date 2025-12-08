import re
file = 'input.txt'
p1_edge_count = 10 if file == 'test.txt' else 1000

lines = open(file).read().split('\n')
coords = [[int(y) for y in re.findall(r"(\d+)", x)] for x in lines]
dists = {}
num_boxes = len(coords)
dist = lambda x,y: (x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2 

for i in range(num_boxes):
    for j in range(i+1, num_boxes):
        d = dist(coords[i], coords[j])
        dists[d] = (i,j)

ccs = [set([i]) for i in range(num_boxes)]
cc_dict = {i:i for i in range(num_boxes)} # index of cc containing i
dist_keys = sorted(dists)
num_ccs = num_boxes
for i in range(len(dist_keys)):
    v1, v2 = dists[dist_keys[i]]
    c1 = cc_dict[v1]
    c2 = cc_dict[v2]
    if c1 != c2:
        ccs[c1] = ccs[c1].union(ccs[c2])
        ccs[c2] = set()
        for j in ccs[c1]:
            cc_dict[j] = c1
        if num_ccs == 2:
            p2ans = coords[v1][0]*coords[v2][0]
        num_ccs -= 1
    if i == p1_edge_count:
        p1ans = 1
        for l in sorted(map(len, ccs), reverse = True)[:3]:
            p1ans *= l
print(f"Part 1: {p1ans}\nPart 2: {p2ans}")