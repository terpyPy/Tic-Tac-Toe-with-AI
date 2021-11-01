# Cameron Kerley
# current build date 11/1/2021 v_2
import random
def makeMove(board, letter, move):
    board[int(move)] = letter


def isWinner(bo, le):
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or  # across the top
            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle
            (bo[0] == le and bo[1] == le and bo[2] == le) or  # across the bottom
            (bo[6] == le and bo[3] == le and bo[0] == le) or  # down the left side
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the middle
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the right side
            (bo[6] == le and bo[4] == le and bo[2] == le) or  # diagonal right
            (bo[8] == le and bo[4] == le and bo[0] == le))    # diagonal left


def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def chooseMoveFromList(board, movesList, letter):
    if letter == 'O':
        opletter = 'X'
    else:
        opletter = 'O'

    if opletter in board and letter not in board:
        if isSpaceFree(board, 4):
            return 4
        else:
            return random.choice(movesList)
    else:
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)
            if isWinner(board, letter):
                possibleMoves.clear()
                possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return 4


def getComputerMove(board, computerLetter):
    board = sum(board, [])
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # Here is our algorithm for our Tic Tac Toe AI
    # fisrt, check to see is we can win this move
    for i in range(len(board)):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):

                return i+1
    # check if the player could win next turn and block them
    for i in range(len(board)):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):

                return i+1
    # Try to take one of the corners, if they are free.
    move = chooseMoveFromList(board, [0, 2, 6, 8], computerLetter)
    move_2 = chooseMoveFromList(board, [1, 3, 5, 7], computerLetter)
    if isSpaceFree(board, move):
        return move+1
    elif isSpaceFree(board, move_2):
        return move+1
    # try the center is all else fails\


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(0, 10):
        if isSpaceFree(board, i):
            return False
    return True
