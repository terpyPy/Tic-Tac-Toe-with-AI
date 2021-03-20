import random
import PySimpleGUI as sg
import permutations as perm

def drawBoard(board):
    #
    # This function prints out the board that it was passed
    # "board" is a list of 10 strings representing the board (ignore index 0)
    BoxFormat = '    |   |'
    boxSep = (' -----------')
    
    print(' ' + board[7] + ' | ' + board[8] , ' | ' + board[9])
    print(boxSep)
    print(' ' + board[4] + ' | ' + board[5] , ' | ' + board[6])
    print(boxSep)
    print(' ' + board[1] + ' | ' + board[2] , ' | ' + board[3])
    print('\n')
def callback():
    return 'X'

def inputPlayerLetter():
    # Lets the player type which letter they want to be
    # Returns a list with the player’s
    # letter as the first item, and the computer's letter as the second.
    #print('do you want to be X or O?:')
    letter = 'X'
    if letter != (letter == 'X' or letter == 'O'):
        letter = letter.upper()


        # the first element
        # in the list is the player’s letter, the second is the computer'spython

    if letter.upper() == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # this returns true if the payer wants to go again
    # otherwise it returns FLase
    #respons = sg.popup('do you want to play again?:', custom_text=('yes', 'no'))
    return 'yes'


def makeMove(board, letter, move):
    board[int(move)] = letter


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal right
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal left


def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board,move):
    
    if move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('what is your next move?: (1-9)')
    return None

def chooseMoveFromList(board, movesList, letter):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
        if isWinner(board, letter):
            possibleMoves.clear()
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)

def getComputerMove(board, computerLetter):
    moveType = 'attack'
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
                moveType = 'attack'
                return i
    # check if the player could win next turn and block them
    for i in range(len(board)):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                moveType = 'block'
                return i 
    # Try to take one of the corners, if they are free.
    move = chooseMoveFromList(board, [1, 3, 7, 9], computerLetter)
    move2 = chooseMoveFromList(board, [2, 4, 6, 8], computerLetter)
    if moveType ==  'attack':
        return move
    elif moveType == 'block':
       return move2
    # try the center is all else fails\
    else:
        return 5 

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

wins = 0
losses = 0
while True:
    # reset the board
    theBoard = [' '] * 10

    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    
    gameIsPlaying = True
    print(wins, ' --Total Wins', losses, ' --Total losses')
    #appName = 'tic-tac-toe'
    #layout = [[sg.Text('welcome to tick tac toe!', key='letter')],
#             [sg.Output(key='out', size=(25,12), font=20, pad=(20/20, 20/20))],
#             [sg.In(),sg.Button('confirm move')], [sg.Button('Next')]
#             ]
    #activeWindow = sg.Window(appName, layout)
    while gameIsPlaying:
        #event, values = activeWindow.read()
        print('player ' + turn)
        if turn == 'player':
            # players turn
            drawBoard(theBoard)
            move = getComputerMove(theBoard, playerLetter)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You win!!!!!')
                gameIsPlaying = False
                wins += 1
            else:
                if isBoardFull(theBoard):
                    #drawBoard(theBoard)
                    print('the game is a tie!!!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                losses += 1
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

        #activeWindow.Element('out').Update(drawBoard(theBoard))
    if playAgain() != 'yes':
        break
