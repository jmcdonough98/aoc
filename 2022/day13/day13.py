def compare(l,r):
    for i in range(min(len(l),len(r))):
        if isinstance(l[i], int) and isinstance(r[i], int):
            if l[i] < r[i]:
                return -1
            if l[i] > r[i]:
                return 1
        elif isinstance(l[i], list) and isinstance(r[i], list):
            tmp = compare(l[i], r[i])
            if tmp != 0:
                return tmp
        elif isinstance(l[i], int) and isinstance(r[i], list):
            tmp = compare([l[i]], r[i])
            if tmp != 0:
                return tmp
        elif isinstance(l[i],list) and isinstance(r[i], int):
            tmp = compare(l[i], [r[i]])
            if tmp != 0:
                return tmp
    return (len(l) > len(r)) - (len(l) < len(r))

def grugSort(signals):
    for i in range(len(signals)):
        for j in reversed(range(1,i+1)):
            if compare(signals[j-1], signals[j]) == 1:
                signals[j-1], signals[j] = signals[j], signals[j-1]
            else:
                break

def day13():
    s = open('input.txt','r').read().split('\n')
    signals = [eval(x) for x in s if x != '']

    count = 0
    for i in range(len(signals)//2):
        if compare(signals[2*i], signals[2*i - 1]) == -1:
            count += i + 1

    print("Part 1:", count)

    signals.append([[2]])
    signals.append([[6]])
    grugSort(signals)

    print("Part 2:", (1+ signals.index([[2]]))*(1 +signals.index([[6]])))

if __name__ == '__main__':
    day13()