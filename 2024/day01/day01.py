print((lambda l,r: (sum(abs(l[i] -r[i]) for i in range(len(l))), sum(a*r.count(a) for a in l)))(*[sorted(l) for l in list(zip(*[tuple(int(y) for y in x.split('   ')) for x in open('input.txt','r').read().split('\n')]))]))