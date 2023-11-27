from collections import defaultdict

def makeGraph(filename):
    V = {}
    E = defaultdict(set)
    bridges = open(filename, 'r').read().split('\n')
    starts = []
    for b in bridges:
        x,y = list(map(int, b.split('/')))
        if x == 0:
            starts.append((x,y))
        V[(x,y)] = False
    for v in V:
        for w in V:
            tmp = set(v).intersection(set(w))
            if v != w and len(tmp) > 0:
                E[v].add(w)
                E[w].add(v)
    return V,E, starts

def find_highest_weight(V,E,starts):
    #modified dfs
    def find_simple_paths(V, E, path, currV, side):
        V[currV] = True
        path = path + [currV]
        paths.append(path)
        for v in E[currV]:
            if not V[v] and currV[side] in v:
                find_simple_paths(V,E, path, v, v.index(currV[side])^1)
        V[currV] = False
        return
    paths = []
    for x in starts:
        find_simple_paths(V,E,[],x,1)
    
    weights = list(map(lambda p: (len(p), sum(sum(x) for x in p)), paths))

    print("Part 1:", max(weights, key = lambda x: x[1])[1])
    print("Part 2:", sorted(weights)[-1][1])

if __name__ == "__main__":
    V,E,starts = makeGraph("input.txt")
    find_highest_weight(V,E,starts)
