
import regex as re

s = open('input.txt','r').read().split('\n')
p1 = r"([1-9])"
p2 = r"((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|[1-9])"
dic = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6","seven":"7","eight":"8","nine":"9"}

parse = lambda l,pattern : list(map(lambda y: y if y.isdecimal() else dic[y], (x[0] for x in re.findall(pattern, l, overlapped=True))))
ans = lambda l,pattern: (lambda x: int(x[0] + x[-1]))(parse(l,pattern))

print(sum(ans(l, p1) for l in s))
print(sum(ans(l, p2) for l in s))

