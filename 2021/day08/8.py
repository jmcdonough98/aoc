lines = open('input.txt','r').read().split('\n')

c = 0
for l in lines:

    tmp = l.split(' | ')[1]
    for t in tmp.split(' '):
        # print(t, len(t))
        if len(t) in [2,4,3,7]:
            # print(tmp, t)
            c+= 1
    # print(tmp)
print(c)

def decode_display(digit, key):
    #easy
    if len(digit) == 2:
        return 1
    if len(digit) == 3:
        return 7
    if len(digit) == 4:
        return 4
    if len(digit) == 7:
        return 8
    decoded = ""
    
#  a
# b c
#  d 
# d e
#  f