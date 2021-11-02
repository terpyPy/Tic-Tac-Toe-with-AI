# Cameron Kerley
# current build date 11/1/2021 v_2
import random
import cpuEvaluate as eval
from bad_version import TTTWith_badcpu as badCPU
def drawBoard(b):
    #
    # This function prints out the board that it was passed
    # "board" is a list of 10 strings representing the board (ignore index 0)
    BoxFormat = '    |   |'
    boxSep = (' -----------')
    for row in range(3):
        print(' ' + b[row][0] + ' | ' + b[row][1] , ' | ' + b[row][2])
        if row <= 1:
            print(boxSep)
    
    print('\n')

def inputPlayerLetter():
    # Lets the player type which letter they want to be
    # Returns a list with the player’s
    # letter as the first item, and the computer's letter as the second.
    print('do you want to be X or O?:')
    letter = str(input())
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
def compileMove(move):
    move = int(move) 
    if move<= 3:
        return [0, move-1]
    elif move >= 3 and move < 7:
        return [1, move-4]
    else:
        return [2, move-7]

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move[0]][move[1]] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, compileMove(move)):
        print('What is your next move? (1-9)')
        move = input()
    return compileMove(move)

def getComputerMove(board, cpuLetter):
    return eval.findBestMove(board, cpuLetter)



def isWinner(bo, le):
    if eval.evaluate(bo,le) == 0:
        return False
    else:
        return True

def playAgain():
    # this returns true if the payer wants to go again
    # otherwise it returns FLase
    #respons = sg.popup('do you want to play again?:', custom_text=('yes', 'no'))
    return 'yes'
def makeMove(board, letter, move):
    board[move[0]][move[1]] = letter

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(3) :    
        for j in range(3) :
            if isSpaceFree(board, [i,j]):
                return False
    return True

def main():
    wins = 0
    losses = 0
    ties = 0
    while True:
    # Reset the board
        theBoard = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            ]
        playerLetter, computerLetter = 'X', 'O'
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        print(' --Total Wins:', wins, ' --Total losses:',losses,  '--total ties:', ties)
        print('player is '+ playerLetter)
        drawBoard(theBoard)
        while gameIsPlaying:
            if turn == 'player':
                print("player turn")
                # Player's turn.
                #move = getPlayerMove(theBoard)
                # print('cpu thinks your best move is: ', getComputerMove(theBoard, playerLetter))
                move = compileMove(badCPU.getComputerMove(theBoard, playerLetter))
                 
                makeMove(theBoard, playerLetter, move)
                drawBoard(theBoard)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    wins += 1
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        ties += 1
                        break
                    else:
                        turn = 'computer'

            else:
                # Computer's turn.
                print("Computer's turn")
                move = getComputerMove(theBoard, computerLetter)
                # move = compileMove(badCPU.getComputerMove(theBoard, computerLetter))
                makeMove(theBoard, computerLetter, move)
                drawBoard(theBoard)
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    losses += 1
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        ties += 1
                        break
                    else:
                        turn = 'player'
            
        if not playAgain():
            break
if __name__ == '__main__':
    # if not imported as a module run the main loop
    main()
