from copy import copy
with open("input.txt","r") as f:
    stream = [int(x) for x in f.read().split(",")]

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
TARGET = 19690720
def readCodes(stream):
    i = 0
    while stream[i] != 99 and i < len(stream):
        if stream[i] == 1:
            stream[stream[i+3]] = stream[stream[i+2]] + stream[stream[i+1]]
        elif stream[i] == 2:
            stream[stream[i+3]] = stream[stream[i+2]] * stream[stream[i+1]]
        i += 4
    return stream

def tryNounVerbPair(stream, n, v):
    stream[1] = n 
    stream[2] = v 
    stream = readCodes(stream)
    return stream[0]


def findCorrectNounVerb(stream,maxN):
    for n in range(maxN):
        for v in range(maxN):
            res = tryNounVerbPair(copy(stream),n,v)
            if res == TARGET:
                return 100*n + v
    return -1 # not found   


#### Animation ####
def makeAnimation(stream):
    i = 0
    ims = []
    while stream[i] != 99 and i < len(stream):
        if stream[i] == 1:
            stream[stream[i+3]] = stream[stream[i+2]] + stream[stream[i+1]]
        elif stream[i] == 2:
            stream[stream[i+3]] = stream[stream[i+2]] * stream[stream[i+1]]
        im = plt.imshow(np.array(stream).reshape(11,11), animated = True)
        ims.append([im])
        i += 4

    fig = plt.figure(1)
    ani = animation.ArtistAnimation(fig, ims, blit=True,)

    # Black magic to get the image to save with no border (still doesn't completely work)
    plt.gca().set_axis_off()
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
                hspace = 0, wspace = 0)
    plt.margins(0,0)

    ani.save('test.gif',writer='imagemagick',savefig_kwargs={"bbox_inches":"tight","pad_inches":0})
print("PART 1:", tryNounVerbPair(copy(stream),12,2))
print("PART 2:", findCorrectNounVerb(copy(stream),100))
makeAnimation(stream)