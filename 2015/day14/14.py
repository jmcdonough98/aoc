
reindeer =[(22,8,165), (8,17,114), (18,6,103), (25,6,145), (11,12,125), (21,6,121), (18,3,50), (20,4,75), (7,20,119),]
def findDistance(v,t,rest, total):
    d = 0
    ct = 0
    while ct + t < total:
        d += v*t 
        ct += t + rest 
    if ct < total:
        d += v*(total - ct)
    return d

def itereindeer(reindeer):
    resting = [False]*len(reindeer)
    counters = [0]*len(reindeer)
    points = [0]*len(reindeer)
    distances = [0]*len(reindeer)
    for t in range(2503):
        for i,r in enumerate(reindeer):
            if not resting[i]:
                distances[i] += r[0]
                counters[i] += 1
                if counters[i] == r[1]:
                    counters[i] = 0
                    resting[i] = True
            else:
                counters[i] += 1
                if counters[i] == r[2]:
                    counters[i] = 0
                    resting[i] = False
            #update distances
        
        points[distances.index(max(distances))] += 1
    print(points,distances)
    return max(points)
maxDist = 0
for r in reindeer:
    d = findDistance(r[0],r[1],r[2],2503)
    if d > maxDist:
        maxDist = d 

print(maxDist)
print(itereindeer(reindeer))
