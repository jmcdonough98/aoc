s = open('input.txt', 'r').read().split('\n\n')

balls = [int(x) for x in s[0].split(',')]
boards = []
for tmp in s[1:]:
    tmp2 = tmp.split('\n')
    for i in range(len(tmp2)):
        tmp2[i] = [int(x) for x in tmp2[i].split(' ') if x != '']
    boards.append(tmp2)

def removeFromAll(boards,n):
    for i in range(len(boards)): 
        boards[i] = removeVal(boards[i],n)

def removeVal(board,n):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == n:
                board[i][j] =0
    return board
def scoreBoard(b):
    for i in range(len(b)):
        if sum(b[i]) == 0:
            return True 
    for i in range(len(b)):
        if sum([x[i] for x in b]) == 0:
            return True 
    return False 
def simulateGames(balls, boards):
    fc = 0
    finished = [False]*len(boards)
    for ball in balls:
        removeFromAll(boards,ball)
        for i,board in enumerate(boards):
            if scoreBoard(board) and (not finished[i]):
                finished[i] = True
                fc += 1
                if fc == 1:
                    print("PART 1:", sum([sum(x) for x in board])*ball)
                if fc == len(boards):
                    print("PART 2:", sum([sum(x) for x in board])*ball)
                    return

simulateGames(balls,boards)