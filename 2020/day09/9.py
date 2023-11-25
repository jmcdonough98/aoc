s = [int(x) for x in open('input.txt','r').read().split('\n')]

def isValid(s,n,i):
    for j in range(n+1):
        for k in range(n+1):
            if i != j and s[i] == s[i-j]+ s[i-k]:
                return True
    return False
def p1(s,n):
    for i in range(n+1,len(s)):
        if not isValid(s,n,i):
            return (i,s[i])
def p2(target,index):
    for i in range(index):
        for j in range(index):
            tmp = s[i:j+1]
            if sum(tmp) == target:
                return min(tmp) + max(tmp)

index,ans = p1(s,25)
ans2 = p2(ans,index)
print(ans,ans2)
