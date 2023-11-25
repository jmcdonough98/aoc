_input = open('input.txt','r') .read().split('\n')
s = [set(x[:len(x)//2]).intersection(set(x[len(x)//2:])) for x in _input]
score = lambda x: 27 + ord(x) - ord('A') if ord('A') <= ord(x) <= ord('Z') else ord(x) - ord('a') + 1
print(sum(score(t.pop()) for t in s))
print(sum(score(set(_input[i]).intersection(set(_input[i+1])).intersection(set(_input[i+2])).pop()) for i in range(0,len(_input)-2,3)))