
class Directory:
    def __init__(self,parent,_id):
        self.id = _id
        self.parent = parent
        self.children = []
        self.totalsize = 0
    def updateSize(self):
        self.totalsize = 0
        for c in self.children:
            if isinstance(c,Directory):
                c.updateSize()
                self.totalsize += c.totalsize
            else:
                self.totalsize += c[0]
    def navigate(self,newID):
        for d in self.children:
            if isinstance(d, Directory) and d.id == newID:
                return d

def parseCommands(s):
    flatDirs = [Directory(None, "/")] # keep list of references for easier access later ^_^
    currentDir = flatDirs[0]
    i = 1
    while i < len(s):
        line = s[i]
        if line[:4] == "$ cd":
            if line == "$ cd ..":
                currentDir = currentDir.parent
                pass
            else:
                currentDir = currentDir.navigate(line[5:])
        if line[:4] == "$ ls":
            lsline = "a"
            while i +1< len(s) and s[i+1][0] != "$":
                i += 1
                lsline = s[i].split(' ')
                if lsline[0] == 'dir':
                    newDir = Directory(currentDir, lsline[1])
                    currentDir.children.append(newDir)
                    flatDirs.append(newDir)
                else:
                    currentDir.children.append((int(lsline[0]), lsline[1] ))
        i += 1
    return flatDirs

def part1(flatDirs):
    flatDirs[0].updateSize()
    print("Part 1:", sum(x.totalsize for x in flatDirs if x.totalsize <= 100000))

def part2(flatDirs):
    neededSpace = flatDirs[0].totalsize - 40000000
    candidates = [f for f in flatDirs if f.totalsize - neededSpace > 0]
    print("Part 2:", min(candidates, key = lambda x:  x.totalsize - neededSpace).totalsize)

def day7():
    flatDirs = parseCommands(s)
    part1(flatDirs)
    part2(flatDirs)

if __name__ == '__main__': 
    s = open('input.txt','r').read().split('\n')
    day7()