sec = 20201227
cardPub = 3418282
doorPub = 8719412
def encode(msg,loopSize):
    enc = 1
    for i in range(loopSize):
        enc = (enc * msg) % sec
    return enc

def findLoopSize(pub):
    i = 0
    msg = 7
    enc = 1
    while enc != pub:
        enc = (enc * msg) % sec
        i += 1
    return i
l1 = findLoopSize(cardPub)
l2 = findLoopSize(doorPub)
print(encode(encode(7,l1),l2))