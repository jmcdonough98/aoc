from collections import defaultdict
s = open('input.txt','r').read().split('\n\n')

def day6():
    c = 0
    c2 = 0
    for group in s:
        questions = defaultdict(int)
        people = 1
        for char in group:
            if char != '\n':
                questions[char] += 1
            else:
                people += 1
        for q in questions:
            if people == questions[q]:
                c2 += 1
        c+= len(questions)
    return c,c2

    
print(day6())