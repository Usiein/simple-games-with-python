# REVERSI

import sys
import random

def drawBoard(board):
    # This function prints out the board that it was passed. Returns None.
    HLINE = ' +--------+'
    # VLINE = '  |   |   |   |   |   |   |   |   |'
    print('  12345678')
    print(HLINE)
    for y in range(8):
        # print(VLINE)
        print('%s|' % (y + 1), end = '')
        for x in range(8):
            print(board[x][y], end = '')
        print('|')
        # print(VLINE)
    print(HLINE)

def resetBoard(board):
    # Blanks out the board it is passed, except for the original starting position.
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    # Starting pieces.
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

def getNewBoard():
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board

def isValidMove(board, tile, xstart, ystart):
    # Returns False if the player's move on space xstart, ystart is invalid.
    # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    board[xstart][ystart] = tile # temporarily set the tile on the board.
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'
    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1],
                                   [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # first step in the direction
        y += ydirection # first step in the direction
        if isOnBoard(x, y) and board[x][y] == otherTile:
            # There is a piece belonging to the other player next to our piece.
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    # Brea out of while loop, then continue in for loop.
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction
                # until we reach the original space, noting all the tiles
                # along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[xstart][ystart] = ' ' # restore the empty space
    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move
        return False
    return tilesToFlip

def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <= 7

def getBoardWithValidMoves(board, tile):
    # Returns a new board with . marking a possible moves the player can make.
    dupeBoard = getBoardCopy(board)

    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '.'
    return dupeBoard

def getValidMoves(board, tile):
    # Return a list of [x, y] lists of valid moves for the given player on the board.
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enterPlayerTile():
    # Let the player type in which tile they want to be.
    # Returns a list with the player's tile as the first item, and the computer's tile as the second.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        tile = input('Do you want to be X or O?').upper()

    # The first element in the list is the player's tile, the second is the computer's tile.
    if tile == 'X':
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
    # This function returns True if the player wants to play again, otherwise returns False.
    return input('Do you want to play again? (Y/N)').lower().startswith('y')

def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart and flip any of the opponents pieces
    # Returns False if this is an invalid move, True if it is valid
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    # Make a duplicate of the board list and return the duplicate
    dupeBoard = getNewBoard()

    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]

    return dupeBoard

def isOnCorner(x, y):
    # Returns True if the position is in one of the four corners
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

def getPlayerMove(board, playerTile):
    # Let the player type in their move.
    # Return the move as [x, y] (or returns strings 'Hint' or 'Quit')
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        move = input('Enter your move or type quit/hint: ').lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Type the x digit (1-8), then the \
y digit (1-8)')
            print('For example, 11 will be the top-left corner.')

    return [x, y]

def getComputerMove(board, computerTile):
    # Given the board and the computer's tile determine where to move and
    # return that move as a [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)

    # randomize the order of the possible moves
    random.shuffle(possibleMoves)

    # always go for a corner if available
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Go through all the possible moves and remember the best scoring move
    bestScore = -1
    bestMove = []
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def showPoints(playerTile, computerTile):
    # Prints out the current score
    scores = getScoreOfBoard(mainBoard)
    print('You have %s points, Computer have %s points.' % (scores[playerTile],
                                                        scores[computerTile]))

print('Welcome to Reversi!')

while True:
    # Reset the board and game
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    while True:
        if turn == 'player':
            # Player's turn
            if showHints:
                validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
                drawBoard(validMovesBoard)
            else:
                drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            move = getPlayerMove(mainBoard, playerTile)
            if move == 'quit':
                print('Thank\'s for playing!')
                sys.exit()
            elif move == 'hints':
                showHints = not showHints
                continue
            else:
                makeMove(mainBoard, playerTile, move[0], move[1])

            if getValidMoves(mainBoard, computerTile) == []:
                break
            else:
                turn = 'computer'

        else:
            # Computer's turn
            drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            input('Press Enter to see computer\'s move.')
            x, y = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, x, y)

            if getValidMoves(mainBoard, computerTile) == []:
                break
            else:
                turn = 'player'

    # Display the final score
    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    print('X scored %s points, O scored %s points.' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' %
                                (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You lost. The computer beat you by %s points.' %
                                (scores[computerTile] - scores[playerTile]))
    else:
        print('The game is a tie!')

    if not playAgain():
        break
