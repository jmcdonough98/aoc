lines = open('input.txt','r').read().split('\n')
c = 0
score = {')':3, ']':57, '}':1197, '>':25137}
validLines = []
for l in lines:
    stack = []
    broken = False
    for i in range(len(l)):
        if l[i] in ['(','[','{','<']:
            stack.append(l[i])
        else:
            if (l[i] == ')' and stack[-1] != '(') or \
                (l[i] == ']' and stack[-1] != '[') or \
                (l[i] == '}' and stack[-1] != '{') or \
                (l[i] == '>' and stack[-1] != '<'):
                c += score[l[i]]
                broken = True
                break 
            else:
                stack.pop()
    if not broken:
        validLines.append(stack)

s2 = {'(':1,'[':2,'{':3, '<':4}
c2s = []
for v in validLines:
    tmp = 0
    for char in reversed(v):
        tmp *= 5
        tmp += s2[char]
    c2s.append(tmp)
print(c)
print(sorted(c2s)[len(c2s)//2])