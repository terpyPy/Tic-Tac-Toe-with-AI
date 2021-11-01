from itertools import count, permutations
import time
from pprint import pprint as p
#store the start time 
startTime = time.time()
#list with each char position up to 8
def chooseMoveFromList(board, movesList, letter):
    possibleMoves = []
    board = [board[7],board[8],board[9],
            board[4],board[5],board[6],
            board[1],board[2],board[3]
            ]
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
        if isWinner(board, letter):
            possibleMoves.clear()
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        allMoves = perm.lookAtAllMoves(board)
        for ind in range(len(allMoves)):
            count = 0
            while count <= 6:
                compareGames = [allMoves[ind+7],allMoves[ind+8],allMoves[ind+9],
                                allMoves[ind+4],allMoves[ind+5],allMoves[ind+6],
                                allMoves[ind+1],allMoves[ind+2],allMoves[ind+3]
                                ]
                if str(compareGames) in str(board):
                    return random.choice(possibleMoves)



                count += 1
                
def lookAtAllMoves(t):
    for i in range(len(t)):
        if t[i] == [' ']:
            t[i] = ['X']
            break
        else:
            print(t[i])
            continue
    test = permutations(t)
    #init a list for all the permutations combos
    allPossibilities = []
    #iterate over the testPermutation object as a list
    for i in list(test):
        allPossibilities += [i]
    currentTime = (time.time() - startTime)
    print(currentTime) 
    #p(allPossibilities) 
    return allPossibilities   
x= 'x'
y = 'y'
lookAtAllMoves([[x],[y],[y],[x],[y],[x],[y],[x],[y]])

#print the total permutations and total time to calculate
#
