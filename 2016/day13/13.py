def neighbors(x,y):
    ret = [(x+1,y), (x, y+1)]
    if x > 0:
        ret.append((x-1,y))
    if y > 0:
        ret.append((x, y-1))
    return ret

def isOpen(x,y, fav_num):
    tmp = x*x + 3*x + 2*x*y + y + y*y + fav_num
    return not bool(tmp.bit_count() % 2)

def find_shortest_path(fav_num, target):
    dists = {(1,1):0}
    boundary = [(1,1)]
    while target not in dists:
        new_boundary = []
        for d in boundary:
            for (x,y) in neighbors(*d):
                if isOpen(x,y, fav_num) and (x,y) not in dists:
                    dists[(x,y)] = dists[d] + 1
                    new_boundary.append((x,y))
        boundary = new_boundary
    return dists[target], len([x for x in dists if dists[x] <= 50])


if __name__ == "__main__":
    # fav_num = 10 # test
    # target = (7,4)
    fav_num = 1358 # puzzle input
    target = (31, 39)
    p1, p2 = find_shortest_path(fav_num, target)
    print(f"Part 1: {p1}\nPart 2: {p2}")
