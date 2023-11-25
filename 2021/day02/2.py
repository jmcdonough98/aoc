lines = open('input.txt','r').read().split('\n')

x = 0
y = 0
aim = 0
for l in lines:
    _dir, n = l.split(' ')
    n = int(n)
    if _dir == 'down':
        # y -= n 
        aim += n
    elif _dir == 'up':
        # y += n
        aim -= n 
    elif _dir == 'forward':
        x += n 
        y -= aim*n
print(x,y,x*y)