
def sgn(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

def simulate(s, N):
    dirs = {"D": (0,-1), "R":(1,0), "L":(-1,0),"U":(0,1)}
    multidir = lambda x,y : [abs(x[0] - y[0]),abs(x[1] - y[1])]

    bridge = [(0,0) for i in range(N)] #bridge[0] = H, bridge[-1] = T
    visited = set()
    for line in s:
        d, n = line.split(' ')
        currDir = dirs[d]
        for i in range(int(n)):
            bridge[0] = (bridge[0][0] + currDir[0], bridge[0][1] + currDir[1])
            for j in range(N-1):
                if max(multidir(bridge[j],bridge[j+1])) > 1:
                    bridge[j+1] = (bridge[j+1][0] + sgn(bridge[j][0] - bridge[j+1][0]),
                                   bridge[j+1][1] + sgn(bridge[j][1] - bridge[j+1][1]))
            visited.add(bridge[-1])
    return len(visited)


if __name__ == '__main__':
    s = open("input.txt","r").read().split("\n")
    print("Part 1:", simulate(s,2))
    print("Part 2:", simulate(s,10))