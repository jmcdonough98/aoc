import json


with open('input.txt','r') as f:
    obj = json.loads(f.read())
a = []
def traverseJSON(obj,p2):
    if isinstance(obj,dict):
        for k in obj:
            if obj[k] == 'red' and p2:
                return
        for k in obj:
            traverseJSON(k,p2)
            traverseJSON(obj[k],p2)
            
    elif isinstance(obj,list):
        for k in obj:
            traverseJSON(k,p2)
    else:
        # print("ATOM:",obj)
        # print(obj,count)
        if isinstance(obj,int):
            a.append(obj)
    return

traverseJSON(obj,False)
print("PART1:",sum(a))
a = []
traverseJSON(obj,True)
print("PART2:",sum(a))
