from itertools import groupby
test = '1'
inp = '1321131112'
def lookandsay(s):
    ns = ''
    for x in groupby(s):
        ns +=  str(len(list(x[1]))) + x[0]
    return ns

for i in range(50):
    inp = lookandsay(inp)
print(len(inp))
# print(lookandsay('11'))