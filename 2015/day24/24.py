test = [1,2,3,4,5,7,8,9,10,11]
_input = [1,3,5,11,13,17,19,23,29,31,37,41,43,47,53,59,67,71,73,79,83,89,97,101,103,107,109,113,]
def partition(ns):
    target = sum(ns) // 3
    print(target,len(ns))
    
partition(test)
partition(_input)
